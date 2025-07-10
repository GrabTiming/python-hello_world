"""
单元测试
"""
import unittest


class UnitTest(unittest.TestCase):
    
    def add(self, a,b):
        return a+b
    
    def setUp(self):
        print("before all test running")
    def test_add(self):
        self.assertEqual(self.add(1,2),3)

    def tearDown(self):
        print("after all test running")