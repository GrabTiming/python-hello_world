# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/9/24 21:06
"""

def func1(**kwargs):
   print(kwargs)


def main():
    func1(score=100,name="小明")
    func1()


if __name__ == "__main__":
    main()
