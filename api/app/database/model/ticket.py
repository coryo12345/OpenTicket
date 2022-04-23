from ast import For
from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Ticket (Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project')
    status_id = Column(Integer, ForeignKey('statuses.id'))
    status = relationship('Status')
    type_id = Column(Integer, ForeignKey('ticket_types.id'))
    ticket_type = relationship('TicketType')
    title = Column(String)
    description = Column(String)

    def __repr__(self) -> str:
        return f'{self.id} | {self.title}'

    def json(self) -> dict:
        # might want to change this to just be ids to reduce data transfer size
        return {
            'id': self.id,
            'project': self.project.json(),
            'status': self.status.json(),
            'ticket_type': self.ticket_type.json(),
            'title': self.title,
            'description': self.description
        }


class Project (Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    prefix = Column(String(5))
    name = Column(String)
    description = Column(String)

    def json(self) -> dict:
        return {
            'id': self.id,
            'prefix': self.prefix,
            'name': self.name,
            'description': self.description
        }


class TicketType (Base):
    __tablename__ = 'ticket_types'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project')
    name = Column(String(20))
    color = Column(String(6))

    def json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color
        }


class Status (Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project')
    name = Column(String)

    def json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

