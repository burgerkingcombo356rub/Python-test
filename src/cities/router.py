from typing import List, Optional

from fastapi import APIRouter, Query

from .schemas import CitySchema
from .service import CityService

router = APIRouter(
    prefix='/cities',
    tags=['Города']
)


@router.post('/create-city/', summary='Создать город', description='Создание города по его названию')
async def create_city(city: str = Query(description="Название города", default=None)) -> CitySchema:
    return await CityService.create_city(name=city)


@router.get('/get-cities/', summary='Список городов', description='Получение списка городов')
async def cities_list() -> List[CitySchema]:
    return await CityService.find_all()


@router.get('/get-city/', summary='Найти город', description='Получение города по названию')
async def get_city(city_name: str = Query(description="Название города", default=None)) -> Optional[CitySchema]:
    city: dict = {'name': city_name}
    return await CityService.find_one_or_none(**city)
