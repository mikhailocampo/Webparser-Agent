import logging
import os
import sys
from typing import Any, Dict, List, Tuple
from loguru import logger

from app.core.settings.base import BaseAppSettings
from app.core.logging import InterceptHandler


class AppSettings(BaseAppSettings):
    """
    Application settings.
    """

    debug: bool = False
    logging_level: int = logging.INFO
    docs_url: str = "/docs"
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Webparser-Agent API: AI Agent as a Service"
    version: str = "0.0.0"
    api_prefix: str = "/api"
    allowed_hosts: List[str] = ["*"]
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
    authorization: str = "Bearer"
    secret_key: str = os.getenv("SECRET_KEY")

    class Config:
        validate_assignment = True

    def validate_authorization(self, auth_header: str) -> bool:
        """
        Validate the authorization header against the secret key.
        """
        if not auth_header.startswith(self.authorization):
            return False
        _, token = auth_header.split()
        return token == self.secret_key

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "openapi_url": self.openapi_url,
            "docs_url": self.docs_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]
        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])
