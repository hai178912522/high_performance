#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 14:04
# @Author  : ZZZZZHHHHH
# @File    : process_pool.py
# @Software: PyCharm
"""Pool class
apply&apply_async
map&map_async
close join terminate
"""
import time
import os
from multiprocessing import Pool
def task_p(x: int):
    time.sleep(2)
    print(f'Sub Process - {os.getpid()} : task - {x}: Result - {2 ** x}\n')

def run_multi_process():
    print("**********Multi Process**********")
    print(f'Main Process - {os.getpid()}')
    start = time.time()
    pool = Pool(processes=os.cpu_count()-4)
    # for x in range(1,31):
    #     # pool.apply(task_p, args=(x,)) # 串行
    #     pool.apply_async(task_p, args=(x,)) # 并行

    # pool.map(task_p, range(1,3)) # 直接在原地等待
    # pool.map_async(task_p, range(1,31)) # 类似于apply_async，但是返回的是一个迭代器

    print('---run sub process---\n')
    pool.close() # 关闭进程池，不再接受新的进程
    pool.join() # 等待进程池中的所有进程执行完毕
    end = time.time()
    print(f'Main Process - {os.getpid()} : Total Time - {end - start:.3f}s')

if __name__ == '__main__':
    run_multi_process()




