"""
面向对象第一节
"""
class Student:
    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "Student(name={}, age={})".format(self.name, self.age)

    def to_dict(self):
        return {"name": self.name, "age": self.age}

def main():
    s = Student("Mike", 18, "Male")

if __name__ == "__main__":
    main()