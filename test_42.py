"""
验证在函数内导入包的耗时：实际上在第一次运行是会完整执行导入包的逻辑，之后会在缓存中找到对应的包，不会重复导入。
这样做的好处：
延迟加载：
解决循环导入

"""

import functools
import time

def time_log(func):

    @functools.wraps(func)
    def wrapper(*args,**kw):
        start_time = time.time()
        result = func(*args,**kw)
        end_time = time.time()
        print(f'method {func.__name__} running time is {end_time-start_time}')
        return result
    return wrapper


@time_log
def test():
    import math
    print(math.gcd(70,28))
    return math.gcd(70,20)

def main():
    test()
    test()

def add(a:int,b:int) -> int :
    """

    :param a:
    :param b:
    :return:
    """
    return a+b

if __name__ == "__main__":
    main()