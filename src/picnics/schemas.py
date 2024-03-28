from datetime import datetime
from typing import List

from pydantic import BaseModel

from cities.schemas import CitySchema
from users.schemas import UserSchema


class PicnicSchema(BaseModel):
    city_id: int
    time: datetime


class AllPicnicSchema(BaseModel):
    id: int
    city: str
    time: datetime
    users: List[UserSchema] no way bro 
