# -*- coding: utf-8 -*-

# -- Sheet --

# 生成式用法
prices = {
    'apple' : 10,
    'banana' : 5,
    'origle' : 7
}

new_fruit = {key: value for key, value in prices.items() if value > 5}
print(new_fruit)

# oop

class People:
    """abstract class people"""

    def __init__(self, info):
        self.__name = info['name']
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name
    
args = {'name': 'ming', 'sex': 'female', 'age': '20', }
ming = People(args)
print(f'ming:{ming}')
print(f'ming.__doc__:{ming.__doc__}')
print(f'ming.__module__:{ming.__module__}')
print(f'ming.__dict__:{ming.__dict__}')
try:
    print(f'ming.__annotations__:{ming.__annotations__}')
except AttributeError:
        print("'People' object has no attribute '__annotations__'")

ning_inf = {'name': 'ning'}
ning = People(ning_inf)
print(ning.name)

# -- Sheet 2 --

# # lambda use
# 
# >https://www.w3school.com.cn/python/python_lambda.asp
# 
# **re = lambda args: func_content**  
# 无函数名 **args**即为函数参数 **func_content**即为函数体 **re**即为返回值<br>
# 下面的*algrithom* ***lambda return type*** 为 bool


def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

import numpy as np


test_data = np.random.randint(1, 10000, 10000)
sort_data = select_sort(test_data)




# # 这是一个MarkDown
# 这是它的语法教程 [Markdown语法](https://markdown.com.cn)。


