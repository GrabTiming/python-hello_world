# 条件控制语句

## 简单的if else
a = int(input())

if a < 10 :
    print("小于10")
elif a == 10 :
    print("等于10")
else :
    print("大于10")

b = 2
match b :
    case 0 :
        print(0)
    case 1 :
        print(1)
    case 2 :
        print(2)