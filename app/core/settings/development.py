import logging
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "[DEV] Webparser-Agent API"
    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = "dev.env"
