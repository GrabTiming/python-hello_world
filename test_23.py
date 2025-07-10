# 这是一个装饰器的 盲敲 练习 ，因为我
import functools
import time


# 这是不带参数的装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print('%s is running...' % func.__name__)
        result = func(*args, **kwargs)
        print("after running ,the result is %d" % result)
        return result
    return wrapper

# 这是带参数的装饰器
def log_second(log_time = time.time()):

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('time is %s , %s is running...' % (log_time, func.__name__))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# functools 的 wraps 的作用：被修饰的函数，他的元数据会被wrapper覆盖，所以为了解决这个问题，引入了functools.wraps
def log_third(log_time = time.time()):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('time is %s , %s is running...' % (log_time, func.__name__))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@log
def add(a,b):
    return a+b
@log_second(log_time=time.time())
def sub(a,b):
    return a-b

@log_third(log_time=time.time())
def mul(a,b):
    return a*b

def main():
    add(1,2)
    print(add.__name__) # 这里已经被wrapper覆盖了，显示结果为wrapper
    sub(1,2)

    mul(1,2)
    print(mul.__name__) # 还是原来的mul

if  __name__ == '__main__':
    main()