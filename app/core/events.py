from fastapi import FastAPI
from loguru import logger
from typing import Callable
from dotenv import load_dotenv, find_dotenv


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        settings = app.state.settings
        logger.info(f"Starting [{settings.app_env.value}] Mode Application")
        load_dotenv(find_dotenv())

        # Start up Events

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        settings = app.state.settings
        logger.info(f"Stopping [{settings.app_env.value}] Mode application")
        # Shut down events

    return stop_app
