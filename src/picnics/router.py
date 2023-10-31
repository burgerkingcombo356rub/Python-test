import datetime as dt
from typing import List

from fastapi import APIRouter, Query

from .models import Picnic
from .schemas import AllPicnicSchema, PicnicSchema
from .service import PicnicRegistrationService, PicnicService

router = APIRouter(
    prefix='/picnics',
    tags=['Пикники']
)


@router.get('/all-picnics/', summary='Список всех пикников', description='Список всех пикников')
async def all_picnics(
    datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
    past: bool = Query(default=True, description='Включая уже прошедшие пикники')) -> List[AllPicnicSchema]:
    filters = []
    if datetime:
        filters.append(Picnic.time == datetime)
    if past:
        if datetime:
            filters.clear()
            filters.append((Picnic.time <= dt.datetime.now()) | (Picnic.time == datetime))
        else:
            filters.append((Picnic.time <= dt.datetime.now()))
    else:
        filters.append((Picnic.time >= dt.datetime.now()))

    return await PicnicService.all_picnics(*filters)


@router.post('/picnic-add/', summary='Создать пикник', description='Создать пикник')
async def picnic_add(city_id: int = Query(description="ID города"),
                     datetime: dt.datetime = Query(description="Дата пикника", default=None)) -> PicnicSchema:
    picnic = {'city_id': city_id, 'time': datetime}
    await PicnicService.add(**picnic)
    return PicnicSchema(**picnic)


@router.post('/picnic-register/', summary='Регистрация на пикник', description='Регистрация пользователя на пикник')
async def register_to_picnic(user_id: int = Query(description="ID пользователя"),
                             picnic_id: int = Query(description="ID пикника")):
    registration = {'user_id': user_id, 'picnic_id': picnic_id}
    await PicnicRegistrationService.add(**registration)
    return registration
