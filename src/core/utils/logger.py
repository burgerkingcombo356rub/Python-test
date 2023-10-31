import logging
import os

from settings import SETTINGS


class Logger():
    def __init__(self) -> None:
        os.makedirs(os.path.dirname(SETTINGS.PATH_TO_LOG_FILE), exist_ok=True)

        logger = logging.getLogger('uvicorn')
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(SETTINGS.PATH_TO_LOG_FILE)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
