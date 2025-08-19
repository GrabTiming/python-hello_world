# coding = utf-8
import re
import unittest
from typing import List

from entity import Student


class Test(unittest.TestCase):

    def test_is_number(self):
        self.assertTrue(is_number('1'))
        self.assertTrue(is_number('1.0'))
        self.assertTrue(is_number('-1'))
        self.assertTrue(is_number(' 1 '))
        self.assertFalse(is_number(''))
        self.assertFalse(is_number('   '))

    def test_sort_student(self):
        student1 = Student('张三', 18,90.0)
        student2 = Student('李四', 19,80.0)
        student3 = Student('王五', 17,70.0)
        students = [student3, student2, student1]
        sort_student(students)
        self.assertEqual(students, [student1, student2, student3])

    def test_print_student(self):
        # student1 = Student('张三', 18,90.0)
        # print_student(student1)

        # 如果以一个字典传入参数会报错吗
        student2 = {'name': '张三', 'age': 18, 'score': 90.0}
        print_student(student2) #会

    def test_transfer_object_to_dict(self):
        student1 = Student('张三', 18,90.0)
        res = transfer_object_to_dict(student1)
        print(res)
        self.assertEqual(res, {'name': '张三', 'age': 18, 'score': 90.0})

        student2 =Student('张三', 18,None)
        res = transfer_object_to_dict(student2)
        print(res)
        self.assertEqual(res, {'name': '张三', 'age': 18, 'score': None})

def is_number(s:str) -> bool:
    """
    判断一个字符串是否是数值,这里指正常显示的数字，不包括科学计数法
    :param s:
    :return:
    """
    s = s.strip()
    if not s:
        return False
    pattern = r'^[+-]?(\d+\.?\d*|\.\d+)$'
    return bool(re.match(pattern, s))


def transfer_object_to_dict(obj:object):
    return obj.__dict__

def sort_student(students: List[Student]):
    students.sort(key=lambda x: x.score,reverse=True)

def print_student(student: Student):
    print(student.name, student.age,student.score)