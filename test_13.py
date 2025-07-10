import unittest # 单元测试库
from  test_09 import *


class TestAlgorithm(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
    def test_sub(self):
        self.assertEqual(sub(2,1), 2)
