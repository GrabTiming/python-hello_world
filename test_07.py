
# 列表操作
studentList = ['Mike','John','Amy']

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


numberList = [1,4,5,2,3]
# 求最大、最小、总和
print(min(numberList))
print(max(numberList))
print(sum(numberList))

# 获取排序后的列表，但是不会改变原先的列表
print(sorted(numberList))

# 列表推导式 [表达式 for循环]
qlist = [ x**2 for x in numberList]
print(qlist)

# 生成器表达式,每次只生成一个值，是一个迭代器，每次调用会从上一次调用的地方之后进行
generator = (x**2 for x in numberList)
for x in generator:
    print(x)


