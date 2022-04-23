# create engine for each dao type
from .auth import AuthDAO
from .ticket_dao import TicketDAO

auth_engine = AuthDAO()
ticket_engine = TicketDAO()
