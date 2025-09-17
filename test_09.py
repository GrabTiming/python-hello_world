# 函数

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def gcd(a,b):
    if a < b :
        tmp = a
        a = b
        b = tmp
    if b == 0 :
        return a
    return gcd(b, a%b)

def power(x,n = 2) :
    res = 1
    while n > 0 :
        res = res * x
        n = n - 1
    return res

## 在一个list中找到最大和最小的元素，返回tuple
def getMaxAndMin(list):
    if len(list) == 0:
        return None,None
    if len(list) == 1:
        return list[0],list[0]
    
    mx,mn = -1e9,1e9
    for x in list:
        mx = max(mx,x)
        mn = min(mn,x)
    return mx,mn

def foo(* args,** kwargs):
    """
    args 是非关键字参数,以元组形式传进
    kwargs 是关键字参数  以字典形式传进来
    :param args:非关键字参数
    :param kwargs:
    :return:
    """
    print(args)
    print(kwargs)


if __name__=="__main__":
    print()
    print(gcd(9,6))
    print(power(9))
    print(power(9,3))

    list = [10,414,21,3,5]
    print(getMaxAndMin(list))

    foo(1,2,3,x=1,y=2,z=3)