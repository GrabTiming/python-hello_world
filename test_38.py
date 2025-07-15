# 判断1000以内的素数
import math
from typing import List


def get_prime_1():
    """朴素解法"""
    res: List[int] = []
    for i in range(2,1001):
        flag = 0
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0 :
                flag = 1
                break
        if flag == 0:
            res.append(i)
    return res

def get_prime_2():
    """埃氏筛法"""
    res: List[int] = []
    prime_len = 0
    vis: List[bool] = [True for i in range(1001)]
    print(len(vis))
    for i in range(2,1001):
        if vis[i]:
            res.append(i)
            prime_len += 1
        for j in range(prime_len):
            if i * res[j] > 1000:
                break
            vis[i*res[j]] = False
            if i % res[j] == 0:
                break
    return res
def main():
    prime_list1 = get_prime_1()
    print(prime_list1)
    prime_list2 = get_prime_2()
    print(prime_list2)
if __name__ == "__main__":
    main()