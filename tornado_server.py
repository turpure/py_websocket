#! usr/bin/python
# coding:utf8

from tornado import websocket, web, ioloop


class EchoWebSocket(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")
        for i in xrange(10):
            self.write_message(str(i))

    def on_message(self, message):
        for i in range(10):
            self.write_message(u"You said: " + str(i))

    def on_close(self):
        print("WebSocket closed")


def main():
    app = web.Application([
        (r'/', EchoWebSocket)
    ])
    app.listen(8880)
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
