# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/12/25 09:04
"""
from test_47 import sort_student


def main():
   students = [
      {
         "name": "张三",
         "age": 18,
         "sex": "男",
         "score": 60,
      },
      {
         "name": "李四",
         "age": 19,
         "sex": "女",
         "score": 80,
      },
      {
         "name": "王五",
         "age": 20,
         "sex": "男",
         "score": 90,
      },
      {
         "name": "赵六",
         "age": 21,
         "sex": "女",
         "score": 90,
      },
   ]
   # 按一个关键字排序
   sort_students = sorted(students,key=lambda x:x["score"],reverse=True)
   print(sort_students)

   # 按多个关键字排序
   sort_students = sorted(students,key=lambda x: (x["score"],x["age"]),reverse=True)
   print(sort_students)


if __name__ == "__main__":
    main()
