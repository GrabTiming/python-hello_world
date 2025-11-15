# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/19 09:12
"""
from test_62 import log_details


@log_details()
def func(a,b,c,d,*args,**kwargs):
   pass


def main():
   func(1,2,3,4,5,6,7,x=23)


if __name__ == "__main__":
    main()
