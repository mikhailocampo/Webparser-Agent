from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.prod

    class Config:
        env_file = ".env"
