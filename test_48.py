"""
获取一个方法的参数名以及参数值
"""
import functools
import inspect


def log_args():
    def decorator(func):
        @functools.wraps(func)  # 这个的作用是如果函数被装饰器修饰，那就直接调用修饰后的方法而不用显式转换后调用
        def wrapper(*args, **kw):
            # 函数名
            function_name = func.__name__

            # 获取函数的参数签名
            sig = inspect.signature(func)
            # 绑定参数到签名
            bound_args = sig.bind(*args, **kw)
            bound_args.apply_defaults()  # 应用默认值
            # 构建参数字典
            params = {}
            for name, value in bound_args.arguments.items():
                params[name] = value
            print(f"function [{function_name}] args : {params}")
            result = func(*args, **kw)
            return result
        return wrapper

    return decorator

@log_args()
def add(a: int, b: int) -> int:
    return a+b


if __name__ == "__main__":
    add(1,2)

