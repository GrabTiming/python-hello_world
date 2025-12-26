# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/12/25 22:03
"""


class DictToObject(object):
   def __init__(self, data):
      for k, v in data.items():
         setattr(self, k, v)


def main():
   student1 = {
      "name": "Liang",
      "age": 18,
      "sex": "Male",
      "grade": "Junior High School",
   }
   student_object = DictToObject(student1)
   print(student_object.name)

if __name__ == "__main__":
    main()
