# 关于python 3.5之后的typing包的类型
# 这个只是形式上的类型检查，让人知道元素的类型
from typing import List, Dict

if __name__ == "__main__":
    student_list:List[str] = ["Alice","Bob"]
    print(student_list)
    score_map:Dict[str,int] = {
        "Alice": 85,
        "Bob": 37,
        123: 122,
    }