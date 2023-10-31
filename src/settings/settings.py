import os
from os.path import dirname, join
from typing import Optional

from dotenv import load_dotenv

load_dotenv()
dotenv_path = join(dirname(__file__), '.env')


class Settings:
    def __init__(self):
        self.WEATHER_API_KEY: str = self.get_argument('WEATHER_API_KEY')
        self.DATABASE_HOST: str = self.get_argument('DATABASE_HOST')
        self.DATABASE_PORT: str = self.get_argument('DATABASE_PORT')
        self.DATABASE_NAME: str = self.get_argument('DATABASE_NAME')
        self.DATABASE_USER: str = self.get_argument('DATABASE_USER')
        self.DATABASE_PASSWORD: str = self.get_argument('DATABASE_PASSWORD')
        self.LOG_LEVEL: str = self.get_argument('LOG_LEVEL')
        self.PATH_TO_LOG_FILE: str = self.get_argument('PATH_TO_LOG_FILE')

    @property
    def DATABASE_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.DATABASE_USER}:"
                f"{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")

    def get_argument(self, arg):
        argument = os.environ.get(arg)
        if not argument:
            raise ValueError(f'Argument: {arg} not defined in Settigs')
        if argument.isdigit():
            argument = int(argument)
        return argument

SETTINGS = Settings()
