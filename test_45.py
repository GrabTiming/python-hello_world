"""
关于classmethod and staticmethod
classmethod 的第一个参数是类本身
而staticmethod 只是一个方法，只是恰好定义在了类的内部
"""


class Dog:

    @classmethod
    def yell(cls):
        print("wang")


    @staticmethod
    def yell_static():
        print("wang in static")



if __name__ == "__main__":
    Dog.yell()
    Dog.yell_static()