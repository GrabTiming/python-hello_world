"""
实现一个LRU缓存
使用python的有序字典实现：OrderedDict
这个数据结构 维护插入的顺序
move_to_end() 方法可以根据传入的last参数(True/False) 移到末尾或者开头
popItem() 方法根据传入的last参数 移除末尾或者开头的元素

"""
from typing import OrderedDict


class LRUCache:

    def __init__(self,name: str, capacity: int):
        self.cache = OrderedDict()
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"{self.name}: {dict(self.cache)}"


    def get(self,key:str):
        if key not in self.cache:
            return None
        val = self.cache.get(key)
        self.cache.move_to_end(key)
        return val

    def put(self,key:str,val:int):

        self.cache[key] = val
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)



def main():
    cache = LRUCache("student_score",2)
    cache.put("3", 3)
    cache.put("4", 4)
    print(cache)
    cache.put("2", 2)  # 淘汰键 3
    print(cache)
    cache.put("5",5) # 淘汰键4
    print(cache)
    cache.get("2")
    print(cache)

if __name__ == "__main__":
    main()
