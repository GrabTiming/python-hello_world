import unittest


def sort_first(arr: list[int]) :
    """
        selected sort : everytime select the min element from the not sorted list
    """
    n = len(arr)
    if n < 2 :
        return
    for i in range(0,n):
        mn_idx = i
        for j in range(i+1,n):
            if  arr[j] < arr[mn_idx]:
                mn_idx = j
        arr[i],arr[mn_idx] = arr[mn_idx],arr[i]

def sort_second(arr: list[int]):
    """
        bubble sort : every time let the max element  to the end
    """
    n = len(arr)
    if n < 2 :
        return
    r = n - 1
    for i in range(0,r):
        for j in range(0,r-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]

def partition(arr:list[int],l:int,r:int):
    if l >= r :
        return l
    pivot = arr[l]
    i = l-1
    for j in range(l+1,r+1):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1] = pivot
    return i+1

def quick_sort(arr:list[int], l:int,r:int):
    if l >= r :
        return
    pivot = partition(arr,l,r)
    if pivot-1 > l :
        quick_sort(arr,l,pivot-1)
    if pivot+1 < r:
        quick_sort(arr,pivot+1,r)


def sort_third(arr: list[int]):
    quick_sort(arr,0,len(arr)-1)




class TestSort(unittest.TestCase):
    def test_sort_first(self):
        arr = [6, 5, 4, 3, 2, 1]
        sort_first(arr)
        res = sorted(arr)
        self.assertEqual(arr, res)

    def test_sort_second(self):
        arr = [6, 5, 4, 3, 2, 1]
        sort_second(arr)
        res = sorted(arr)
        self.assertEqual(arr, res)

    def test_sort_third(self):
        arr = [6, 5, 4, 3, 2, 1, 7, 2, 1, 4, 2, 5, 6, 7]
        sort_third(arr)
        res = sorted(arr)
        self.assertEqual(arr,res)