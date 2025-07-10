# list.sort 和sorted 的区别
"""
list.sort 会原地修改列表，而sorted方法是创建一个新的列表出来
"""

nums = [6,5,3,2,1,4,10,9,8,7]

print("sorted前：",nums)
sorted(nums)
print("sorted后：",nums)

print("sort方法前：",nums)
nums.sort()
print("sorted方法后",nums)


class student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "student(%s,%s)" % (self.name,self.score)
    def __lt__(self,other):
        # 按照student的score 排序
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


student_list = [student("tom",90),student("jack",80),student("lucy",50)]

print(student_list)
student_list.sort()
print(student_list)

# sort有一个key参数，用来传比较函数，reverse参数是否倒序

list2 = [(1,3),(4,2),(5,1),(6,4)]
# 按每个元素的第二个元素排序
list2.sort(key=lambda x:x[1],reverse=True)
print(list2)

# 按长度排序
fruits_list = ["apple","orange","pear","banana","strawberry"]
fruits_list.sort(key=len)
print(fruits_list)