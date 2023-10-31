from typing import Any, Optional

from pydantic import BaseModel


class CitySchema(BaseModel):
    id: Optional[int]
    name: str
    weather: Any
