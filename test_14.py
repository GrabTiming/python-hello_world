# 列表生成式
## 可以通过 [式子 for循环] 的形式生成式子

## 比如 1~10的平方
list1 = [x*x for x in range(1,11)]
print(list1)

## 1~20内的偶数
list2 = [x for x in range(1,21) if x%2==0 ]
print(list2)
