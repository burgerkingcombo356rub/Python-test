from sqlalchemy import between, insert, select

from database import Session


class BaseService:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filters):
        async with Session() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            result = result.scalar_one_or_none()
            return result

    @classmethod
    async def find_all(cls):
        async with Session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            result = result.scalars().all()
            return result

    @classmethod
    async def find_beetween(cls, column, min, max):
        async with Session() as session:
            query = select(cls.model).filter(between(column, min, max))
            result = await session.execute(query)
            result = result.scalars().all()
            return result

    @classmethod
    async def add(cls, **row):
        async with Session() as session:
            query = insert(cls.model).values(**row)
            await session.execute(query)
            await session.commit()
