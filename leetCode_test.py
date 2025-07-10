from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        self.dfs(nums,0,tmp,result)
        return result

    def dfs(self,nums: List[int],idx: int,tmp: List[int],result: List[List[int]]):
        if idx == len(nums):
            result.append(list(tmp))
            return
        self.dfs(nums,idx+1,tmp,result)
        tmp.append(nums[idx])
        self.dfs(nums,idx+1,tmp,result)
        tmp.remove(nums[idx])

def main():
    nums = [1,2,3,4,5]
    s = Solution()
    res = s.subsets(nums)
    for i in range(len(res)):
        print(res[i])
    print(res)

if __name__ == '__main__':
    main()