# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/12/22 08:32
"""




def main():
   da = {
      "name": "Hello",
      "score": 33.3,
      "is_student": True
   }

   db = {
      "name": "Hello",
      "score": 33.3,
      "is_student": True
   }
   fields = ["name","score","is_student","grade"]
   for field in fields:
      a_value = da.get(field)
      b_value = db.get(field)
      print(field,a_value,b_value)
      if a_value != b_value:
         print("字段:",field,"不一致")

if __name__ == "__main__":
    main()
