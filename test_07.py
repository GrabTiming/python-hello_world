import unittest

class Test(unittest.TestCase):

    def test_list(self):
        arr = [1,2,3,4,5,5]
        # 增
        arr.append(6)
        print(arr)
        # 删
        arr.remove(5)
        print(arr)
        # 查
        print(arr[2])
        # 改
        arr[2] = 4
        print(arr)

    def test_set(self):
        arr = {1,2,3,4,5,6,6}
        print(arr)
        print((1 in arr))
        arr.add(7)
        # set 删除之前要确保值在set中
        print(arr.remove(6))
        if 6 in arr:
            print(arr.remove(6))

    def test_dict(self):
        dict1 = {"Alice": 1 , "Bob": 2,"Charlie": 3,"Django": 3,"Emily": 4}
        dict1["Frank"] = 5
        print(dict1)
        dict1.pop("Alice")
        print(dict1)

if __name__ == "__main__":

    # 列表操作
    studentList = ['Mike', 'John', 'Amy']

    # 追加元素
    studentList.append('Bill')
    print(studentList)
    # 删除某个值
    studentList.remove('John')
    print(studentList)

    # 求列表长度
    print(len(studentList))
    # 列表遍历 按元素
    for student in studentList:
        print(student)

    for index, student in enumerate(studentList):
        print(index, student)

    numberList = [1, 4, 5, 2, 3]
    # 求最大、最小、总和
    print(min(numberList))
    print(max(numberList))
    print(sum(numberList))

    # 获取排序后的列表，但是不会改变原先的列表
    print(sorted(numberList))

    # 列表推导式 [表达式 for循环]
    qlist = [x ** 2 for x in numberList]
    print(qlist)

    # 生成器表达式,每次只生成一个值，是一个迭代器，每次调用会从上一次调用的地方之后进行
    generator = (x ** 2 for x in numberList)
    for x in generator:
        print(x)

