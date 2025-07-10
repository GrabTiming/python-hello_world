# python 装饰器，类似于spring的aop，写好装饰器后，以@装饰器名的方式使用
import functools
import time

def log(text):
    def decorator(func):
        @functools.wraps(func) # 这个的作用是如果函数被装饰器修饰，那就直接调用修饰后的方法而不用显式转换后调用
        def wrapper(*args, **kw):
            print('before: %s %s():' % (text, func.__name__))
            result =  func(*args, **kw)
            print('after: %s %s():' % (text, func.__name__))
            return result
        return wrapper
    return decorator

def time_keeper(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start_time = time.time()
            result = func(*args, **kw)
            end_time = time.time()
            print('running time: %s %6f:' % (func.__name__, end_time - start_time))
            return result
        return wrapper
@log('execute')
@time_keeper
def now():
    print('2024-6-1')

def main():
    now()



if __name__ == '__main__':
    main()