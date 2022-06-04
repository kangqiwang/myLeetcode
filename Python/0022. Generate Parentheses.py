'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left,right,ans= n,n,[]
        self.dfs(left,right,ans,"")
        return ans
    def dfs(self,left,right,ans,string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")
            
print(Solution().generateParenthesis(3))