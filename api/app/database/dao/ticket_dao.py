# Database access for auth functionality
from ..model.ticket import Ticket
from .base_dao import BaseDAO
from sqlalchemy.orm import Session
from sqlalchemy import select


class TicketDAO (BaseDAO):
    def get_all_tickets(self) -> list:
        with Session(self.engine) as session:
            tickets = session.scalars(select(Ticket)).all()
            return [ticket.json() for ticket in tickets]
