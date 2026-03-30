from __future__ import annotations

from typing import TYPE_CHECKING

from .backends import VisualizationBackend
from .cache import VisGenCache
from .models import VisGenOutput, VisualizationRequestRecord
from .programs import (
    DEFAULT_REFINE_ROLLOUTS,
    DEFAULT_REFINE_THRESHOLD,
    build_observed_refine_generator,
    run_generation,
)
from .signatures import ReviewVisualizationImplementation, WriteVisualizationCode

if TYPE_CHECKING:
    import dspy


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
    ) -> list[VisGenOutput]:
        examples = [self.backend.build_example(req) for req in requests]
        cache = VisGenCache.for_runtime(
            backend=self.backend,
            coder_signature=self.coder_signature,
            review_signature=self.review_signature,
            reviewer_lm=self.reviewer_lm,
            refine_rollouts=DEFAULT_REFINE_ROLLOUTS,
            refine_threshold=DEFAULT_REFINE_THRESHOLD,
        )
        cached_outputs, indexed_misses = cache.get_many(examples)

        if indexed_misses:
            fresh_examples = [example for _, example in indexed_misses]
            generator = build_observed_refine_generator(
                backend=self.backend,
                coder_signature=self.coder_signature,
                review_signature=self.review_signature,
                reviewer_lm=self.reviewer_lm,
            )
            fresh_outputs = run_generation(
                generator,
                fresh_examples,
                num_threads=num_threads,
            )
            cache.put_many(fresh_examples, fresh_outputs)
            for (index, _), output in zip(indexed_misses, fresh_outputs):
                cached_outputs[index] = output

        return [output for output in cached_outputs if output is not None]
