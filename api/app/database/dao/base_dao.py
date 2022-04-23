from os import environ
from sqlalchemy import create_engine, engine


class BaseDAO:
    def __init__(self) -> None:
        self.host = environ['DB_HOST']
        self.port = environ['DB_PORT']
        self.dbname = environ['POSTGRES_DB']
        self.username = environ['POSTGRES_USER']
        self.password = environ['POSTGRES_PASSWORD']
        self.init_engine()

    def init_engine(self) -> engine:
        self.engine = create_engine(
            f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.dbname}')
        return self.engine

    def __repr__(self) -> str:
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.dbname}'
