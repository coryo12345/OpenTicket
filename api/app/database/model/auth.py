from .base import Base
from sqlalchemy import Column, Integer, String


class User (Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __repr__(self) -> str:
        return f'{self.id} | {self.username} | {self.password}'

    def json(self) -> dict:
        return {
            'username': self.username,
            'password': self.password
        }
