from app.core.settings.app import AppSettings
import os
import logging


class ProdAppSettings(AppSettings):
    debug: bool = False
    logging_level: int = logging.INFO
    x_api_key: str = os.getenv("X_API_KEY")

    class Config(AppSettings.Config):
        env_file = "prod.env"
