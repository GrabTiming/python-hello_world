"""
python 解包: 取出可迭代的对象中的所有元素
"""


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    d = {'a':1,'b':2,'c':3,'d':4}
    print(arr)
    print(*arr)
    print(d)
    print(*d)

    # 解包 可以用在将一个字典中的元素加到另外一个字典中
    d2 = {'e': 5,'f':6,'g':7}
    d2.update(d)
    print(d2)

    d3 = {**d,**d2}
    print(d3)
