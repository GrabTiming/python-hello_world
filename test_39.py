"""递归练习"""
from typing import Dict

"""斐波那契数列"""

f :Dict[int,int] = {}

def fibonaci(num:int) -> int :
    if num <= 2 :
        return 1
    if num in f:
        return f[num]

    res = fibonaci(num-1)+fibonaci(num-2)
    f[num] = res
    return res

if __name__ == "__main__":
    for i in range(1,21):
        print(fibonaci(i))
