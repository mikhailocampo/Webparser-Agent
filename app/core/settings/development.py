import logging
import os
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "[DEV] Webparser-Agent API"
    logging_level: int = logging.DEBUG
    x_api_key: str = os.getenv("X_API_KEY")

    class Config(AppSettings.Config):
        env_file = "dev.env"
