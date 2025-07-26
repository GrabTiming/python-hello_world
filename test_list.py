"""这个文件专门记录一些列表的操作"""
from typing import List



def kth_largest_element(arr: list,k:int) -> int :
    """
    >>> kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 2)
    5.6
    >>> kth_largest_element([-2, -5, -4, -1], 1)
    -1
    >>> kth_largest_element([], 1)
    Traceback (most recent call last):
    ...
    ValueError: k must less than n
    """
    n = len(arr)
    if n < k :
        raise ValueError('k must less than n')
    l = 0
    r = n-1
    while l<=r:
        pivot_index = partition(arr,l,r)
        if pivot_index == k -1 :
            return arr[pivot_index]
        elif pivot_index > k-1 :
            r = pivot_index-1
        else :
            l = pivot_index +1
    return -1


def partition(arr:list,l:int,r:int):
   if l >= r :
       return l
   pivot = arr[r]
   i = l - 1

   for j in range(l,r):
       if arr[j] >= pivot:
           i += 1
           arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[r] = arr[r],arr[i+1]
   return i + 1

if __name__ == "__main__":
    import doctest

    doctest.testmod()

