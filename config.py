"""Secure configuration management using environment variables from `.env` file."""

import os
from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


def _get_env_path(env_file: str = ".env") -> str:
    """Returns the absolute path to the specified `.env` file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, env_file)


class EnvConfig(BaseSettings):
    """Defines environment variables with validation and defaults."""

    ALPHA_API_KEY: str = Field(..., min_length=1, description="AlphaVantage API key (required)")

    model_config = SettingsConfigDict(
        env_file=_get_env_path(),
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra variables in .env
    )


try:
    # Load and validate environment variables
    settings = EnvConfig()
except ValidationError as e:
    raise RuntimeError(f"Invalid environment variables: {e}") from e