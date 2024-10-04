from app.core.settings.app import AppSettings
import logging


class ProdAppSettings(AppSettings):
    debug: bool = False
    logging_level: int = logging.INFO

    class Config(AppSettings.Config):
        env_file = "prod.env"
