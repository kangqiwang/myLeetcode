'''


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


'''
import numbers
from turtle import left, right
from typing import List
from winreg import REG_NOTIFY_CHANGE_ATTRIBUTES



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # fast=len(nums)-1
        # slow=1
        res=[]
        print(nums)
        for i in range(len(nums)-2):
            if nums[i]>0: break
            if i>0 and nums[i]==nums[i-1]: continue
            left=i+1
            right = len(nums)-1
            # print("left:    "+str(left))
            # print("right:    "+str(right))
            # print("i:   "+str(i))
            while left<right:
                if nums[left]+nums[right]+nums[i]>0:
                    right=right-1
                elif nums[left]+nums[right]+nums[i]<0:
                    left=left+1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while left<right and nums[left] == nums[left-1]: left=left+1
                    while left<right and nums[right] == nums[right+1]:right = right -1
                    

        return res
    
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>0: break
            if nums[i] == nums[i-1]: continue
            left= i+1
            right=len(nums)-1
            while right>left:
                if nums[i]+nums[left]+nums[right] >0:
                    right-=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while right>left and nums[left] == nums[left-1]: left+=1
                    while right>left and nums[right] == nums[right+1]:right-=1
        return res
print(Solution().threeSum1([-1,0,1,2,-1,-4]))