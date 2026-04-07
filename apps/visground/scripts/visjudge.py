# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi>=0.115.0",
#     "peft",
#     "pillow",
#     "torch",
#     "transformers",
#     "uvicorn>=0.30.0",
# ]
# ///

"""
Single-file server implementation to expose inference
over https://huggingface.co/xypkent/visjudge-7b model via HTTP API.

Deployed on a self-managed H100 node. This script might fail on other hardware.
"""

from __future__ import annotations

import base64
import binascii
import logging
from contextlib import asynccontextmanager
from functools import lru_cache
from io import BytesIO
from time import perf_counter
from typing import TypedDict

import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from peft import PeftModel
from PIL import Image, UnidentifiedImageError
from pydantic import BaseModel, ConfigDict, Field
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration

BASE_MODEL_ID = "Qwen/Qwen2.5-VL-7B-Instruct"
ADAPTER_ID = "xypkent/visjudge-7b"

logger = logging.getLogger(__name__)


class ServiceRunInput(TypedDict):
    image: Image.Image
    prompt: str


class PreparedRunInput(TypedDict):
    image: Image.Image
    text: str


class RunRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    image_base64: str = Field(min_length=1)
    prompt: str = Field(min_length=1)


class RunResponse(BaseModel):
    result: str


class RunManyRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    inputs: list[RunRequest] = Field(min_length=1)


class RunManyResponse(BaseModel):
    results: list[str]


class HealthResponse(BaseModel):
    status: str = "ok"


class VisJudgeService:
    def __init__(self) -> None:
        init_started_at = perf_counter()
        logger.info(
            "Initializing VisJudgeService base_model=%s adapter=%s",
            BASE_MODEL_ID,
            ADAPTER_ID,
        )

        base_model_started_at = perf_counter()
        base_model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            BASE_MODEL_ID,
            torch_dtype=torch.bfloat16,
            device_map={"": 0},
        )
        logger.info(
            "Loaded base model in %.2fs",
            perf_counter() - base_model_started_at,
        )

        adapter_started_at = perf_counter()
        model = PeftModel.from_pretrained(
            base_model,
            ADAPTER_ID,
        )
        model = model.merge_and_unload()
        model.eval()
        self._model = model
        logger.info(
            "Loaded and merged adapter in %.2fs",
            perf_counter() - adapter_started_at,
        )

        processor_started_at = perf_counter()
        processor = AutoProcessor.from_pretrained(
            BASE_MODEL_ID,
            padding_side="left",
            min_pixels=512 * 28 * 28,
            max_pixels=2048 * 28 * 28,
        )
        self._processor = processor
        logger.info(
            "Loaded processor in %.2fs",
            perf_counter() - processor_started_at,
        )
        logger.info(
            "VisJudgeService ready in %.2fs device=%s dtype=%s",
            perf_counter() - init_started_at,
            self._model.device,
            self._model.dtype,
        )

    def run(
        self,
        image: Image.Image,
        prompt: str,
        *,
        max_new_tokens: int = 512,
    ) -> str:
        return self.run_many(
            [{"image": image, "prompt": prompt}],
            max_new_tokens=max_new_tokens,
        )[0]

    def run_many(
        self,
        inputs: list[ServiceRunInput],
        *,
        max_new_tokens: int = 512,
    ) -> list[str]:
        if not inputs:
            raise ValueError("inputs must contain at least one item")

        prompt_lengths = [len(item["prompt"]) for item in inputs]
        run_started_at = perf_counter()
        logger.info(
            (
                "Starting inference batch_size=%d prompt_chars_min=%d "
                "prompt_chars_max=%d max_new_tokens=%d"
            ),
            len(inputs),
            min(prompt_lengths),
            max(prompt_lengths),
            max_new_tokens,
        )

        prepare_started_at = perf_counter()
        prepared_inputs = [self._prepare_input(item) for item in inputs]
        batch = self._processor(
            text=[item["text"] for item in prepared_inputs],
            images=[item["image"] for item in prepared_inputs],
            padding=True,
            return_tensors="pt",
        ).to(self._model.device)
        prepare_elapsed = perf_counter() - prepare_started_at

        generate_started_at = perf_counter()
        with torch.inference_mode():
            output_ids = self._model.generate(
                **batch,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                use_cache=True,
            )
        generate_elapsed = perf_counter() - generate_started_at

        generated_ids = [
            output[len(input_ids) :]
            for input_ids, output in zip(batch.input_ids, output_ids)
        ]
        decode_started_at = perf_counter()
        outputs = self._processor.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )
        decode_elapsed = perf_counter() - decode_started_at

        output_lengths = [len(output) for output in outputs]
        logger.info(
            (
                "Finished inference batch_size=%d total=%.2fs prepare=%.2fs "
                "generate=%.2fs decode=%.2fs output_chars_min=%d "
                "output_chars_max=%d"
            ),
            len(inputs),
            perf_counter() - run_started_at,
            prepare_elapsed,
            generate_elapsed,
            decode_elapsed,
            min(output_lengths),
            max(output_lengths),
        )
        return outputs

    def _prepare_input(self, item: ServiceRunInput) -> PreparedRunInput:
        image = item["image"].convert("RGB")
        text = self._processor.apply_chat_template(
            [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image},
                        {"type": "text", "text": item["prompt"]},
                    ],
                }
            ],
            tokenize=False,
            add_generation_prompt=True,
        )
        return {
            "image": image,
            "text": text,
        }


@lru_cache(maxsize=1)
def get_service() -> VisJudgeService:
    logger.info("Creating cached VisJudgeService instance")
    return VisJudgeService()


def decode_image(image_base64: str) -> Image.Image:
    payload = image_base64.strip()
    if "://" in payload and not payload.startswith("data:"):
        logger.warning("Rejected image payload with unsupported URL scheme")
        raise HTTPException(
            status_code=422,
            detail="Only base64 data URLs or raw base64 image payloads are supported.",
        )

    encoded_payload = payload.split(",", maxsplit=1)[-1]
    try:
        image_bytes = base64.b64decode(encoded_payload, validate=True)
    except binascii.Error as exc:
        logger.warning(
            "Rejected image payload with invalid base64 encoding payload_chars=%d",
            len(encoded_payload),
        )
        raise HTTPException(
            status_code=422,
            detail="Invalid base64 image payload.",
        ) from exc

    try:
        image = Image.open(BytesIO(image_bytes))
        image.load()
    except (UnidentifiedImageError, OSError) as exc:
        logger.warning(
            "Rejected image payload that did not decode to a valid image bytes=%d",
            len(image_bytes),
        )
        raise HTTPException(
            status_code=422,
            detail="Decoded payload is not a valid image.",
        ) from exc

    return image


def to_service_run_input(item: RunRequest) -> ServiceRunInput:
    return {
        "image": decode_image(item.image_base64),
        "prompt": item.prompt,
    }


@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.info("Preloading cached VisJudgeService instance at application startup")
    get_service()
    logger.info("Finished preloading cached VisJudgeService instance")
    yield


app = FastAPI(title="VisJudge API", version="1.0.0", lifespan=lifespan)


@app.get("/health", response_model=HealthResponse)
def health_endpoint() -> HealthResponse:
    return HealthResponse()


@app.post("/run", response_model=RunResponse)
def run_endpoint(request: RunRequest) -> RunResponse:
    logger.info("Handling /run request prompt_chars=%d", len(request.prompt))
    service_input = to_service_run_input(request)
    result = get_service().run(
        image=service_input["image"],
        prompt=service_input["prompt"],
    )
    return RunResponse(result=result)


@app.post("/run-many", response_model=RunManyResponse)
def run_many_endpoint(request: RunManyRequest) -> RunManyResponse:
    logger.info("Handling /run-many request batch_size=%d", len(request.inputs))
    results = get_service().run_many(
        [to_service_run_input(item) for item in request.inputs]
    )
    return RunManyResponse(results=results)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)
