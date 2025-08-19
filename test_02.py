# 数学运算
from math import sqrt

a = 1
b = 2
c = 3
d = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b) # 乘方，结果为实数
print(sqrt(d)) # 平方根，结果为实数

x = 5
y = 2
z = x/y
zz = x//y
print(f"{z} {type(z)}")
print(f"{zz} {type(zz)}")


# 0 和 1 可以与bool类型对比，但其他的数值与布尔类型对比都为false
print(1 == True)
print(0 == False)
print(1.0 == True)

print(1 == 1.0)
