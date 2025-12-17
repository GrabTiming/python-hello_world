# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/12/16 21:24

猴子有香蕉666根，每次最多背66根香蕉，可是猴子每走1米要吃1根香蕉，问猴子最多能走多远？

"""
import json
import math


def get_remain_number(origin_num:int, current_num:int, dis:int) -> int:
    """

    :param origin_num: 起点的香蕉数量
    :param current_num: 现在携带的香蕉数量
    :param dis:
    :return: 返回起点再回来能拿到的香蕉数
    """
    if current_num < dis or origin_num < dis:
        return 0
    else:
        return min(origin_num,66)

def work(origin_num:int):
    if origin_num <=66:
        return origin_num

    trips = (origin_num +65) //66
    cost = 2*trips -1
    return max(0,origin_num- cost)



def main():
    origin_num = 666
    dis = 0
    res = 0
    while origin_num > 0:
        if origin_num <=66:
            dis += origin_num
            break
        res = max(res,dis+min(origin_num,66))
        origin_num = work(origin_num)
        dis+=1
        print(dis,origin_num)
    print(dis)


if __name__ == "__main__":
    main()
