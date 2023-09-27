import logging
from functools import lru_cache

from pydantic.v1 import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)


@lru_cache()
def get_setting() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
