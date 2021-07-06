# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 10:27 上午
# @File    : threading_practice.py
# @Software: PyCharm


# threading local data

import time
import threading

local_data = threading.local()


def save_log():

    print(threading.current_thread(), local_data.value)
    print(id(threading.current_thread()))


def target_run(value):

    local_data.value = value
    time.sleep(3)
    print(threading.current_thread().name, local_data.value)
    save_log()


def main():

    t1 = threading.Thread(target=target_run, args=(3,))
    t2 = threading.Thread(target=target_run, args=(6,))
    t3 = threading.Thread(target=target_run, args=(9,))
    t4 = threading.Thread(target=target_run, args=(12,))
    t5 = threading.Thread(target=target_run, args=(15,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()



if __name__ == '__main__':
    main()


