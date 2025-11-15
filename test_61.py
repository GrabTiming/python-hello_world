# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/5 23:41
"""
from functools import reduce



def main():
    pass
    func1 = lambda x: x*2
    list1 = [1,2,3,4]
    # map 函数使用规则
    list2 = list(map(func1,list1))
    print(list2)

    # reduce 函数使用规则
    list3 = [1,2,3,4]
    res = 0
    res = reduce(lambda x,y: x+y,list3)
    print(res)


if __name__ == "__main__":
    main()
