'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    def dfs(self, nums,index,path,res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                tmp='.'*len(nums)
                self.dfs(nums, index+1,path+[tmp[:i]+"Q"+tmp[i+1:]],res)
    
    def valid(self, nums,n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] ==nums[n]:
                return False
        return True
    
print(Solution().solveNQueens(3))