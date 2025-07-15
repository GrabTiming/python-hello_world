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
    if len(s) == 0 :
        return ""

    cur_c = s[0]
    cur_len = 1
    res = []
    for c in s[1:]:
        if c == cur_c:
            cur_len +=1
        else:
            res.append(f"{cur_c}{cur_len}")
            cur_c = c
            cur_len = 1
    res.append(f"{cur_c}{cur_len}")
    turn_str = "".join(res)
    return turn_str if len(turn_str)<len(s) else s


if __name__ == "__main__":
    pass