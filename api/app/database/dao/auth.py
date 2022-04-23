# Database access for auth functionality
from ..model.auth import User
from .base_dao import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import select


class AuthDAO (BaseDAO):
    def get_users(self) -> list:
        with Session(self.engine) as session:
            users = session.scalars(select(User)).all()
            return [user.json() for user in users]
