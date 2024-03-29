'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        nums = set(nums)
        maxi = 0
        for num in nums:
            if num not in my_dict.keys():
                prev_ = my_dict.get(num-1, 0)
                next_ = my_dict.get(num+1, 0)
                my_dict[num] += prev_ + next_ + 1
                my_dict[num-prev_] = my_dict[num]
                my_dict[num+next_] = my_dict[num]
                maxi = max(maxi, my_dict[num])
        return maxi
    def longestConsecutive_1(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

    def longestConsecutive_my(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            if num-1 not in nums:
                nextNum = num+1
                while nextNum in nums:
                    nextNum=nextNum+1
                result = max(result,nextNum-num)
    


Solution().longestConsecutive_1([100,4,200,1,3,2,-1,0])