# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 6:40 下午
# @File    : aioredis_practice.py
# @Software: PyCharm

import aioredis
import asyncio
import random

loop = asyncio.get_event_loop()


async def create_redis():
    redis_conn = await aioredis.create_redis(('127.0.0.1', 6379), db=6)
    set_res = await redis_conn.setnx(key="name", value="kayb")
    print(set_res)
    get_res = await redis_conn.get(key="name")
    print(get_res)


async def get_redis_pool():
    redis_pool = await aioredis.create_redis_pool(('127.0.0.1', 6379), db=6)
    return redis_pool


async def for_write_redis():
    redis_pool = await get_redis_pool()

    i = 0
    while True:
        save_res = await redis_pool.setnx(f"name{i}", value=f"kayb{i}")
        print(save_res)
        i += 1

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(create_redis_pool())
    loop.run_until_complete(for_write_redis())

    # IOLoop.instance().add_callback(create_redis_pool)
    # IOLoop.instance().start()
