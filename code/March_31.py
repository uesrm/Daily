# -*- coding: utf-8 -*-

# -- Sheet --

s = 'aaavfgghhh'
new_s = set(s)
print(s, new_s)
type(new_s)

iter_s = iter(s)
type(iter_s)

# # 迭代器与生成器
# - 生成器一定是迭代器，但迭代器不一定是生成器
# - 迭代器的作用是构建迭代对象后，不会把变量一次性加载入内存，而是call by need，类似滚动数组模式
# - 生成器使用关键词yield，有生成器函数与表达式两种模式
# - **。。。没理解有啥用**


import send
def frange(start, end, step):
    num = start
    while num < end:
        yield num
        num += step

h = frange(1.0, 5.0, 0.5)
next(h)

