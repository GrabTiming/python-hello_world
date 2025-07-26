"""
这个文件专门记录 字符串操作的函数
"""
from typing import List


def reverse(s:str) -> str:
    """字符串反转"""
    res = s[::-1]
    return res

# 字符串压缩 比如"aabb" -> "2a2b"
def short_str(s:str) -> str :
    """
    >>> short_str("aabb")
    '2a2b'
    >>> short_str("bbccaaa")
    '2b2c3a'
    >>> short_str("bb")
    '2b'
    """
    if len(s) == 0 :
        return ""

    cur_c = s[0]
    cur_len = 1
    res = []
    for c in s[1:]:
        if c == cur_c:
            cur_len +=1
        else:
            res.append(f"{cur_len}{cur_c}")
            cur_c = c
            cur_len = 1
    res.append(f"{cur_len}{cur_c}")
    turn_str = "".join(res)
    return turn_str if len(turn_str)<=len(s) else s

def str_split(s:str):
    s_list = s.split('.')
    for item in s_list:
        print(item)

if __name__ == "__main__":
    import doctest

    doctest.testmod()