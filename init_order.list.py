# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/16 08:35

关于初始化的顺序 菱形规则 mro规则

"""


class A:

    def __init__(self):
        print("A")

class B(A):

    def __init__(self):
        print("从B进入")
        super().__init__()
        print("B")

class C(A):

    def __init__(self):
        print("从C进入")
        super().__init__()
        print("C")

class D(B, C):

    def __init__(self):
        super().__init__()
        print("D")


def main():
    D()
    print(D.mro())


if __name__ == "__main__":
    main()
