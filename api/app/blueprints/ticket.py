from flask import Blueprint
from ..database.dao.dao_factory import ticket_engine

ticket = Blueprint('ticket', __name__)


@ticket.route('/all', methods=['GET'])
def status():
    # TODO filter by project id
    return {'data': ticket_engine.get_all_tickets()}

# get all projects
# get ticket types by project
# get ticket statuses by project

# create project
# create ticket
# create status
# create ticket type

# delete project
# delete ticket
# delete status
# delete ticket type

# modify project
# modify ticket
# modify status
# modify ticket type
