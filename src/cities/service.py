from fastapi import HTTPException

from core.service import BaseService
from core.utils.external_requests import CheckCityExisting

from .models import City
from .schemas import CitySchema


class CityService(BaseService):
    model = City

    @classmethod
    async def create_city(cls, name: City):
        if name is None:
            raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
        check = CheckCityExisting()
        if not check.check_existing(name):
            raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

        city_object = await CityService.find_one_or_none(name=name)
        if city_object is None:
            await CityService.add(name=name)
            city_object = await CityService.find_one_or_none(name=name)

        return CitySchema(id=city_object.id, name=city_object.name, weather=city_object.weather)

NYC after LA