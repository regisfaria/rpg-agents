"""Shared LLM provider configuration for the A2A agents."""

import os
from pathlib import Path

from dotenv import load_dotenv
from strands.models.bedrock import BedrockModel
from strands.models.ollama import OllamaModel


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPOSITORY_ROOT / ".env")


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} must be set in {REPOSITORY_ROOT / '.env'}")
    return value


def build_model():
    """Build the model selected by LLM_PROVIDER in the repository .env file."""
    provider = _required("LLM_PROVIDER").lower()

    if provider == "ollama":
        return OllamaModel(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            model_id=_required("OLLAMA_MODEL_ID"),
        )

    if provider == "bedrock":
        has_profile = bool(os.getenv("AWS_PROFILE", "").strip())
        has_keys = bool(
            os.getenv("AWS_ACCESS_KEY_ID", "").strip()
            and os.getenv("AWS_SECRET_ACCESS_KEY", "").strip()
        )
        if not has_profile and not has_keys:
            raise RuntimeError(
                "Set AWS_PROFILE or AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY "
                f"in {REPOSITORY_ROOT / '.env'}"
            )

        return BedrockModel(
            region_name=_required("AWS_REGION"),
            model_id=_required("BEDROCK_MODEL_ID"),
        )

    raise RuntimeError("LLM_PROVIDER must be either 'ollama' or 'bedrock'")
