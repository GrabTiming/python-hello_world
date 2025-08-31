# coding=utf-8
"""
空字符、空的列表和字典 在 判断的时候都会判断为False
"""

if __name__ == '__main__':

    s1 = ""
    if s1:
        print("s1 is not empty")
    list1 = []
    if list1:
        print("list1 is not empty")
    d1 = {}
    if d1:
        print("d1 is not empty")




