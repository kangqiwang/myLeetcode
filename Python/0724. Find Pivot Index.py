'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


'''
from re import I
from turtle import left, right
from typing import List


class Solution:
    # broken support case ""
    
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)-1):
            print(nums[:i])
            print(nums[i+1:])
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            elif sum(nums[:i]) ==0 or sum(nums[i+1:])==0:
                return 0
    
    def pivotIndex1(self, nums: List[int]) -> int:
        left=0
        right = sum(nums)
        for key,value in enumerate(nums):
            right-=value
            if left == right:
                return key
            left+=value
        return -1
            
            
            

print(Solution().pivotIndex1([2,1,-1]))
