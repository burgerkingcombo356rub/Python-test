from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database import Base


class Picnic(Base):
    """
    Пикник
    """
    __tablename__ = 'picnics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    time = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Пикник {self.id}>'


class PicnicRegistration(Base):
    """
    Регистрация пользователя на пикник
    """
    __tablename__ = 'picnic_registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    picnic_id = Column(Integer, ForeignKey('picnics.id'), nullable=False)

    user = relationship('User', backref='picnics')
    picnic = relationship('Picnic', backref='users')

    def __repr__(self):
        return f'<Регистрация {self.id}>'

Call me later pls
