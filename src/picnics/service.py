from itertools import groupby
from operator import itemgetter
from typing import List

from sqlalchemy import select

from cities.models import City
from core.service import BaseService, Session
from users.models import User
from users.schemas import UserSchema

from .models import Picnic, PicnicRegistration
from .schemas import AllPicnicSchema


class PicnicRegistrationService(BaseService):
    model = PicnicRegistration


class PicnicService(BaseService):
    model = Picnic

    @classmethod
    async def all_picnics(cls, *filters):
        async with Session() as session:
            result = []
            query = select(User.id, User.name, User.surname, User.age,
                        cls.model.id.label('picnic_id'), City.name.label('city_name'), cls.model.time
                    ).filter(
                        *filters
                    ).outerjoin(
                        PicnicRegistration, User.id==PicnicRegistration.user_id
                    ).join(
                        cls.model, cls.model.id==PicnicRegistration.picnic_id
                    ).join(
                        City, cls.model.city_id==City.id
                    ).order_by('picnic_id')
            query = await session.execute(query)
            rows = []
            for row in query:
                rows.append(row._asdict())
            grouped_data = groupby(rows, key=lambda x: x['picnic_id'])

            for _, group in grouped_data:
                group_rows = list(group)

                result.append(
                    AllPicnicSchema(
                        id=group_rows[0]['picnic_id'],
                        city=group_rows[0]['city_name'],
                        time=group_rows[0]['time'],
                        users=[UserSchema(id=user['id'],
                                          name=user['name'],
                                          surname=user['surname'],
                                          age=user['age']) for user in group_rows]))
            return result
