"""
关于魔术方法
"""


class Vector:

    def __init__(self,x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__dict__}"

    def __add__(self, other):
        if type(other) is not self.__class__:
            raise Exception(f"can not calculate with this type {type(other)}")
        res = Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return res

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other,self.z * other)

    # 这个函数是为了处理当前类对象在右侧时，前面的变量没有实现与该类的运算逻辑的情况
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

def main():
    v1 = Vector(1,2,3)
    print(v1)
    v2 = Vector(2,3,4)
    print(v1+v2)
    v3 = v1 * 2
    print(v3)
    # 如果没有 __rmul__ 函数会报错
    v4 = 3 * v1
    print(v4)

if __name__ == "__main__":
    main()