"""
yield 关键字的用法
"""

def foo():
    print('111')
    yield 1  # yield 后面带返回值结果
    print('222')
    yield 2
    print('333')
    yield 3

def main():
    # 错误用法: 初学者以为这是调用了函数，实际上带有yield的函数都变成了生成器函数，其返回的是生成器对象
    foo()
    print(type(foo()))

    # 正确用法
    f = foo()
    for i in f:
        print(i)

if __name__ == '__main__':
    main()
