# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/9/28 23:05

魔法函数学习：
__init__ 初始化函数
__add__ 加运算
__eq__ 判断相等运算
__ne__ 判断不相等逻辑
__str__ 转字符串运算

__call__ 类创建时调用
"""

class MyNumber:

   def __init__(self,num: int|float):
      self.num = num

   def __add__(self, other):
      res = MyNumber(self.num + other.num)
      return res

   def __str__(self):
      return f"{self.num}"

   def __eq__(self, other):
      return self.num == other.num

   def __ne__(self, other):
      return self.num != other.num

class Student:

   def __init__(self, name: str, age: int):
      self.name = name
      self.age = age

   def __call__(self, *args, **kwargs):
      print(args)

      print(kwargs)
      country = kwargs.get("country","China")

      print(f"{self.name} is {self.age} years old. I'm from {country}")


def main():
   a = MyNumber(1)
   b = MyNumber(2)
   c = a + b
   print(c)
   print(a == b)
   print(c == b)
   d = MyNumber(3)
   print(c == d)

   s1 = Student("Liang", 18)
   s1(country="America")

if __name__ == "__main__":
    main()
