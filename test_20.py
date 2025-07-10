# collections.deque 用法
"""
特点：deque线程安全，在频繁增加删除元素的场景下比list耗时短
"""
from collections import deque


dq = deque()
dq.append(1) # 从右端加入元素
dq.appendleft(2) # 从左端加入元素

print(dq)

x = dq.pop() # 从右端移除元素
y = dq.popleft() # 从左端移除元素

print(x)
print(y)