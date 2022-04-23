from flask import Flask
from app.blueprints.auth import auth
from app.blueprints.ticket import ticket

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(ticket, url_prefix='/ticket')

if __name__ == '__main__':
    app.run()
