# -*- coding: utf-8 -*-
from flask import session, Flask,render_template
from flask_socketio import SocketIO
import time
from model.app import create_app
from model.database import DataBase
import settings

# SETUP
app = create_app()
socketio = SocketIO(app)


# used for user communication
@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server
    and sending message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """
    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)


# MAINLINE
if __name__ == "__main__":  # start the web server
    socketio.run(app, debug=True, host=str(settings.Config.SERVER))