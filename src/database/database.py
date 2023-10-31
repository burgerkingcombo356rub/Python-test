from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import SETTINGS

engine = create_async_engine(SETTINGS.DATABASE_URL)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()
