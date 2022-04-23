from flask import Blueprint
from ..database.dao.dao_factory import auth_engine

auth = Blueprint('auth', __name__)


@auth.route('/status', methods=['GET'])
def status():
    # TODO will do auth later
    return {'loggedIn': 'false'}


@auth.route('/users', methods=['GET'])
def getUsers():
    return {'data': auth_engine.get_users()}
