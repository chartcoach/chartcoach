from __future__ import annotations

import logging
from typing import TYPE_CHECKING, cast

from .backends import VisualizationBackend
from .cache import VisGenCache
from .models import VisGenResult, VisualizationRequestRecord
from .programs import (
    DEFAULT_RETRY_ITERATIONS,
    build_observed_feedback_loop_generator,
    output_to_result,
    result_to_output,
    run_generation,
)
from .signatures import ReviewVisualizationImplementation, WriteVisualizationCode

if TYPE_CHECKING:
    import dspy

logger = logging.getLogger(__name__)


class VisGenRunner:
    def __init__(
        self,
        backend: VisualizationBackend,
        coder_signature: type[dspy.Signature] = WriteVisualizationCode,
        review_signature: type[dspy.Signature] = ReviewVisualizationImplementation,
        reviewer_lm: dspy.LM | None = None,
    ):
        self.backend = backend
        self.coder_signature = coder_signature
        self.review_signature = review_signature
        self.reviewer_lm = reviewer_lm

    def generate(
        self,
        requests: list[VisualizationRequestRecord],
        num_threads: int = 20,
    ) -> list[VisGenResult]:
        examples = [self.backend.build_example(req) for req in requests]
        cache = VisGenCache.for_runtime(
            backend=self.backend,
            coder_signature=self.coder_signature,
            review_signature=self.review_signature,
            reviewer_lm=self.reviewer_lm,
            retry_iterations=DEFAULT_RETRY_ITERATIONS,
        )
        cached_outputs, indexed_misses = cache.get_many(examples)
        total_requests = len(requests)
        cache_hits = total_requests - len(indexed_misses)
        results: list[VisGenResult | None] = [
            output_to_result(output) if output is not None else None
            for output in cached_outputs
        ]

        execution_slots = 0
        duplicate_miss_fanout = 0
        if indexed_misses:
            grouped_misses: dict[str, list[int]] = {}
            miss_examples_by_key: dict[str, dspy.Example] = {}
            for index, example in indexed_misses:
                key = cache.cache_key(example)
                grouped_misses.setdefault(key, []).append(index)
                miss_examples_by_key.setdefault(key, example)

            miss_keys = list(grouped_misses)
            execution_slots = len(miss_keys)
            duplicate_miss_fanout = len(indexed_misses) - execution_slots
            fresh_examples = [miss_examples_by_key[key] for key in miss_keys]
            generator = build_observed_feedback_loop_generator(
                backend=self.backend,
                coder_signature=self.coder_signature,
                review_signature=self.review_signature,
                reviewer_lm=self.reviewer_lm,
                max_iterations=DEFAULT_RETRY_ITERATIONS,
            )
            fresh_outputs = run_generation(
                generator,
                fresh_examples,
                num_threads=num_threads,
            )
            cache_examples_to_put: list[dspy.Example] = []
            cache_outputs_to_put = []
            for key, result in zip(miss_keys, fresh_outputs, strict=True):
                if output := result_to_output(result):
                    cache_examples_to_put.append(miss_examples_by_key[key])
                    cache_outputs_to_put.append(output)

                for index in grouped_misses[key]:
                    results[index] = cast(VisGenResult, dict(result))

            if cache_examples_to_put:
                cache.put_many(cache_examples_to_put, cache_outputs_to_put)

        logger.info(
            "🧠 VisGen batch | admitted=%s | 💾 cache=%s | 🚀 execute=%s | ♻️ deduped=%s | ✅ ok=%s | ❌ failed=%s",
            total_requests,
            cache_hits,
            execution_slots,
            duplicate_miss_fanout,
            sum(
                1
                for result in results
                if result is not None and result["generation_error"] is None
            ),
            sum(
                1
                for result in results
                if result is not None and result["generation_error"] is not None
            ),
        )

        return [
            result
            if result is not None
            else {
                "id": request["id"],
                "code": None,
                "visualization_type": None,
                "grounding_trace": None,
                "generation_error": "Generation result missing.",
            }
            for request, result in zip(requests, results, strict=True)
        ]
