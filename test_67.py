# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/12/25 09:00
"""
from collections import Counter


def main():
   test_dict = {
      "A": 2,
      "B": 3,
      "C": 4,
   }
   counter1 = Counter(test_dict)
   print(counter1["A"])

   test_list = ["A","A","A","C","C","B","B","D","D","E","F","G"]
   counter2 = Counter(test_list)
   print(counter2)



if __name__ == "__main__":
    main()
