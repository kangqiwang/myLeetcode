'''

You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.


5
4
[1,2,4]
[1,3]


'''
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def getMaxGap(nums, max_size):
            maxGap = max(nums[0], max_size - nums[-1])
            for i in range(1, len(nums)):
                maxGap = max(maxGap, nums[i] - nums[i - 1])
            return maxGap
        return getMaxGap(sorted(horizontalCuts), h) * getMaxGap(sorted(verticalCuts), w) % 1000000007
    
    
print(Solution().maxArea(5,4,[1,2,4],[1,3]))