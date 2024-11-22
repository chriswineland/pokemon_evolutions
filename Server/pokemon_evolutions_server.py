from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from Server.rest_service_adapter import add_rest_services

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'passw0rd'

socketio = SocketIO(app)
socketio.run(app)

add_rest_services(app)

app.run(port=4000)
