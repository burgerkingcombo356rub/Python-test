from typing import Optional

from sqlalchemy import Column, Integer, String

from core.utils.external_requests import GetWeatherRequest
from database import Base


class City(Base):
    """
    Город
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    @property
    def weather(self) -> Optional[str]:
        """
        Возвращает текущую погоду в этом городе
        """
        r = GetWeatherRequest()
        weather: Optional[str] = r.get_weather(self.name)
        return weather

    def __repr__(self):
        return f'<Город "{self.name}">'

Hello my friend 
