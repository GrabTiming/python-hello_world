# coding = utf-8
#!/usr/bin/env python

"""
验证yield 调试
"""
import time


def test(x:int) ->int:
    if x %2 == 0 :
        return x*2
    else:
        return 0

def main():

    print("hello")
    for i in range(5):
        result = yield test(i)
        print(result)

    time.sleep(10)


if __name__== "__main__":
    main()