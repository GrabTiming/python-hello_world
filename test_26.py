"""
面向对象第二节,类的继承
"""

class Person(object):

    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print(self):
        print(self.name, self.age, self.sex)


class Student(Person):

    def __init__(self, name, age,sex, grade,school):
        super().__init__(name, age,sex)
        self.grade = grade
        self.school = school

    def print(self):
        print("大家好，我叫%s,今年%d岁，是%s一名学生" % (self.name, self.age, self.school))


def main():
    p = Person("小明", 18, "男")
    p.print()
    s = Student("小红", 18, "女", 3, "北理工")
    s.print()


if __name__ == '__main__':
    main()