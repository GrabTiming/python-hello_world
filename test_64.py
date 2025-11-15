# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
@Author : Liang2003
@Time   : 2025/11/15 10:15
"""

"""
枚举类的好处： 输入规定外的值时IDE会提示
"""


from enum import Enum


class StudentLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class Student:
    def __init__(self, name: str, level: StudentLevel):
        self.name = name
        self.level = level

    def __str__(self):
        return f"Student {self.name} is at level {self.level.value}"

def main():
    student = Student("Alice", StudentLevel.INTERMEDIATE)
    student2 = Student("Bob", StudentLevel.ADVANCED)
    student3 = Student("DDD", "error")
    print(student)
    print(student2)


if __name__ == "__main__":
    main()
