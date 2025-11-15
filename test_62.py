# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/10/18 09:04

装饰器练习
1. 用于打印执行函数的参数信息
2. 重试装饰器
3. 权限校验装饰器
"""
import functools
import random
import unittest


# ===========================  打印函数参数 =======================================

def log_details(text=""):

   def decorator(func):

      @functools.wraps(func)
      def wrapper(*args, **kwargs):
         print(f"正在执行 {func.__name__} 函数")
         print(f"参数列表为 {args},{kwargs}")
         result = func(*args, **kwargs)
         print(f"执行结果: {result}")
         return result
      return wrapper
   return decorator

@log_details()
def add(a:int,b:int,c:int,d:int=0):
   return a + b + c + d


# ===========================  重试 =======================================

def retry(times=3,expect_val=None):
   """重试装饰器，返回是否成功"""
   def decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
         for i in range(times):
            try:
               result = func(*args, **kwargs)
               if expect_val is None or result == expect_val:
                  print(f"retry {i+1} times and success")
                  return True
            except Exception as e:
               print(f"第{i+1}次重试")
               print(e)
         print(f"retry {times} times and fail")
         return False
      return wrapper
   return decorator

@retry(expect_val=True)
def test2():
   rand_num = random.randint(0,10)
   if rand_num > 5:
      return True
   else:
      return False


# ===========================  权限校验 =======================================

def auth_name():
   """权限校验装饰器"""
   def decorator(func):

      @functools.wraps(func)
      def wrapper(*args, **kwargs):
         # 权限校验根据不同场景需要做出变换，下面做个简单的name的校验
         if args:
            self = args[0]
            if hasattr(self,"__class__") and hasattr(self,'name'):
               if self.name == "Liang":
                  print("校验通过，执行方法")
                  func(*args, **kwargs)
                  return True
         print("校验失败")
         return False
      return wrapper
   return decorator


class User:
   def __init__(self,name:str,permission: list):
      self.name = name
      self.permission = permission

   @auth_name()
   def run(self):
      print(f"{self.name} 正在操作")


class DecoratorTest(unittest.TestCase):

   def test_log_details(self):
      result = add(1,2,3,d=4)
      self.assertEqual(result,10)

   def test_retry(self):
      result = test2()
      self.assertEqual(result,True)

   def test_auth_name(self):
      user = User("Admin",["add","delete"])
      user.run()

