"""扔骰子， 6000次，统计每个点数出现的次数"""
import random
from typing import Dict


def main():
    res:Dict[int,int] = {}
    for cnt in range(6000):
        i = random.randint(1,6)
        val = res.get(i,0)
        res[i] = val+1
    for key,value in res.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    main()