
# 729. 我的日程安排表 I
## 题意：要求给出多个[l,r)区间，问添加下一个[l,r)区间会不会与前面的有重合，

from sortedcontainers import SortedDict

class MyCalendar:

    def __init__(self):
        ## 有序字典,key值存放end，value存放start，
        self.sd = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.sd.bisect_right(startTime) ## 找到第一个结束时间大于start的区间
        if idx < len(self.sd) and self.sd.values()[idx] < endTime:
            return False
        self.sd[endTime] = startTime
        return True