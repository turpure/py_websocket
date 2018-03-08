#! usr/bin/python
# coding:utf8

import time
from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)


@sockets.route('/')
def hello(ws):
    while not ws.closed:
        time.sleep(1)
        now = time.time()
        ws.send(str(now).encode())


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('127.0.0.1', 8880), app, handler_class=WebSocketHandler)
    server.serve_forever()
