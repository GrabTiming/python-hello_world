# 高阶函数
from functools import reduce

## map(f,list) 将list中的元素通过f函数转换得到一个Iterator
list1 = [1,2,3,4,5]
def pow(x):
    return x*x

print(list(map(pow,list1)))


## reduce(f,list)中f接收两个参数，每次迭代的结果作为下一次的第一个参数继续迭代

def add(x,y):
    return x+y
print(reduce(add,list1))

## filter

print(list(filter(lambda x:x%2==1,list1)))
## sorted
list2 = [2,5,1,3,4]
list2 = sorted(list2)
print(list2)

## lambda函数  一般是参数变换成其他结果
list3 = [1,2,3,4,5]
list3 = list(map(lambda x:x ** 2,list3))
print(list3)