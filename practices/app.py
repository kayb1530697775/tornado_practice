# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 5:17 下午
# @File    : hello_world.py
# @Software: PyCharm
import random
import contextvars

request_id = contextvars.ContextVar('request_id')

import asyncio

from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from aioredis_practice import for_write_redis

common_num = list()


class IndexHandler(RequestHandler):
    def get(self):
        print('hello world')
        self.write('hello world')


class ForWriteRedisHandler(RequestHandler):
    async def get(self):

        write_res = await for_write_redis()

        self.write(str(write_res))


def save_db_to(num):
    print(num, request_id.get())


class Cxt1Handler(RequestHandler):
    async def get(self):
        common_num.append('3')
        await asyncio.sleep(5)
        random_str = str(random.randint(100, 999))
        print(1, 'random_str', random_str)
        request_id.set(random_str)
        save_db_to(1)
        self.write(f"{''.join(common_num)}")


class Cxt2Handler(RequestHandler):
    async def get(self):
        common_num.append('6')
        # await asyncio.sleep(10)
        random_str = str(random.randint(100, 999))
        print(2, 'random_str', random_str)
        request_id.set(random_str)
        save_db_to(2)

        self.write(f"{''.join(common_num)}")


if __name__ == '__main__':
    app = Application([
        (r"/", IndexHandler),
        (r"/for_write", ForWriteRedisHandler),
        (r"/cxt1", Cxt1Handler),  # 上下文管理
        (r"/cxt2", Cxt2Handler),  # 上下文管理
    ])

    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start(2)  # mul process
    IOLoop.instance().start()

