from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

auth = HTTPBasicAuth()


users = {
    app.config['BASE_AUTH_USER']: generate_password_hash(app.config['BASE_AUTH_PASSWORD']),
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


import routes
