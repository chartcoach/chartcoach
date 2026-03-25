import os

import dspy


def lm_cliproxy(model: str) -> dspy.LM:
    return dspy.LM(
        f"openai/{model}",
        api_base="http://localhost:8317/v1",
        api_key="sk-",
    )


def lm_openrouter(model: str) -> dspy.LM:
    return dspy.LM(
        f"openai/{model}",
        api_base="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )


dspy.configure_cache(
    enable_disk_cache=True,
    enable_memory_cache=True,
    disk_size_limit_bytes=16 * 1024 * 1024 * 1024,
)
