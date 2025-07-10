# 面向对象
class Animal:
    # 构造函数，注意方法名__init__ 是无法改变的，约定俗成的
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name+": 吃饭")


## 继承 通过在类名后面(父类)实现继承

class Dog(Animal):
    def __init__(self, name):
        ## 使用父类的构造方法
        super().__init__(name)
    def eat(self):
        print(self.name+": 吃肉")

dog1 = Dog("旺财")
dog1.eat()

