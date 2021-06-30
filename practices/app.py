# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 5:17 下午
# @File    : hello_world.py
# @Software: PyCharm


from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        print('hello world')
        self.write('hello world')


if __name__ == '__main__':
    app = Application([
        (r"/", IndexHandler)
    ])

    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start(2)  # mul process
    IOLoop.instance().start()

