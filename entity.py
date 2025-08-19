"""
用于记录练习用的实体
"""

class Person(object):
    """描述一个人会有哪些属性"""
    def __init__(self,name:str,age:int,height:float = 0,weight:float = 0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Student(Person):

    def __init__(self, name: str, age: int, height: float, weight: float, score: float = 0):
        super().__init__(name, age, height, weight)
        self.score = score

