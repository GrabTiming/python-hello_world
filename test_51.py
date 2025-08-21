# -coding = utf-8
"""
学习可变参数
*args : 这个表现的形式是list
**kwargs : 这个表现的形式一个dict
"""
import unittest


def sum(*nums):

    res = 0
    for num in nums:
        res = res + num
    return res

def print_student_score(**kwargs):
    print(kwargs)


class Test(unittest.TestCase):

    def test_sum(self):
        x = sum(1,2,3)
        self.assertEqual(x,6)
        y = sum(1,2,3,5)
        self.assertEqual(y,11)

    def test_1(self):
        print_student_score(x=1,y=2,z=3)