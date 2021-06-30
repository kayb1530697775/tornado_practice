# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 5:37 下午
# @File    : async_http_client.py
# @Software: PyCharm


from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient


async def async_request():
    async_http = AsyncHTTPClient()
    response = await async_http.fetch('http://www.baidu.com')
    print(response.body.decode('U8'))


if __name__ == '__main__':
    IOLoop.instance().spawn_callback(async_request)
    IOLoop.instance().start()

    # IOLoop.run_sync(async_request)
