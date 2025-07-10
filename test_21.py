"""
reduce 函数的用法，该函数的作用是在迭代过程中当前元素与之前的结果交互的过程
"""
from functools import reduce

numbers = [6,5,4,3,2,1]

mul_res = reduce(lambda a,b : a*b,numbers)
add_res = reduce(lambda a,b : a+b,numbers)
print("%d %d" % (mul_res,add_res))