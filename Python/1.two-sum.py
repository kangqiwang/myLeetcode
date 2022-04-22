#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums.pop(0)
            if a in nums:
                return [i, nums.index(a)+i+1]

    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            print(map)   
            if nums[i] not in map:
                map[target - nums[i]] = i 
            else:
                return [map[nums[i]], i]
        return [-1, -1]
   
print(Solution().twoSum2([3,14,2,7],9))
