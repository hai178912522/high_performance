#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 13:22
# @Author  : ZZZZZHHHHH
# @File    : process_and_threads.py
# @Software: PyCharm
import time
import os
from multiprocessing import Process
from threading import Thread, current_thread  # 告诉你当前线程的名字


def task_p(x: int):
    time.sleep(2)
    print(f'Sub Process - {os.getpid()} : task - {x}: Result - {2 ** x}\n')


def task_t(x: int):
    time.sleep(2)
    print(f'Sub Thread - {current_thread().name} : task - {x}: Result - {2 ** x}\n')


def run_single_process():
    print("**********Single Process**********")
    print(f'Main Process - {os.getpid()}')
    start = time.time()
    task_p(1)
    task_p(2)
    end = time.time()
    print(f'Main Process - {os.getpid()} : Total Time - {end - start:.3f}s')


def run_single_thread():
    print("**********Single Thread**********")
    print(f'Main Thread - {current_thread().name}')
    start = time.time()
    task_t(1)
    task_t(2)
    end = time.time()
    print(f'Main Thread - {current_thread().name} : Total Time - {end - start:.3f}s')


def run_multi_process():
    print("**********Multi Process**********")
    print(f'Main Process - {os.getpid()}')
    start = time.time()
    p1 = Process(target=task_p, args=(1,))  # tuple
    p2 = Process(target=task_p, args=(2,))  # tuple
    print('---run sub process---\n')
    p1.start()
    p2.start()
    p1.join()  # wait for p1 to finish
    p2.join()  # wait for p2 to finish
    end = time.time()
    print(f'Main Process - {os.getpid()} : Total Time - {end - start:.3f}s')


def run_multi_thread():
    print("**********Single Thread**********")
    print(f'Main Thread - {current_thread().name}')
    start = time.time()
    t1 = Thread(target=task_t, args=(1,))  # tuple
    t2 = Thread(target=task_t, args=(2,))  # tuple
    print('---run sub thread---\n')
    t1.start()
    t2.start()
    t1.join()  # wait for t1 to finish
    t2.join()  # wait for t2 to finish

    end = time.time()
    print(f'Main Thread - {current_thread().name} : Total Time - {end - start:.3f}s')


if __name__ == '__main__':
    # run_single_process()
    # run_multi_process()
    # run_single_thread()
    run_multi_thread()
