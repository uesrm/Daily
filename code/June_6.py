# -*- coding: utf-8 -*-

# -- Sheet --

# 装饰器用法

import random
import time

def decorate(func):
    
    def record(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        use_time = end - start
        print(f'{func.__name__} waste time: {use_time} s')
        return result
    
    return record


@decorate
def down_load(file_name):
    T = random.randint(0, 10)
    time.sleep(T)
    print(f'random time: {T} s\ndownload {file_name} completed')



# TODO learn collections : solved
# TODO learn itertools : unsolved

from collections import namedtuple

import hashlib 

def main():
    
    down_load('从头到尾学摄影.avi')
    
    Card = namedtuple('Card', ('suite', 'face'))
    card1 = Card('红桃', '5')

    print(hashlib.md5('nsjfugfntbtghg'.encode()).hexdigest())



