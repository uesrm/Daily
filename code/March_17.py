# -*- coding: utf-8 -*-

# -- Sheet --

def bubble_sort(items, comp = lambda x, y: x > y):
    """
        冒泡顺序排序 前移版
    """
    item = items[:]
    for i in range(len(item) - 1):
        swapped = False
        for j in range(len(item) - 1 - i):
            if comp(item[j], item[j + 1]):
                item[j], item[j + 1] = item[j + 1], item[j]
                swapped = True
        if not swapped:
            break
    return item

import numpy as np

test_data = np.random.randint(1, 1000, 100)
sort_data = bubble_sort(test_data)



