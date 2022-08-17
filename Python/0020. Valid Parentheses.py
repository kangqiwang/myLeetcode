'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


'''


from inspect import stack
from pickletools import read_unicodestring1


class Solution:
    def isValid(self, s: str) -> bool:
        opened= ["[","(","{"]
        closed = ["]",")","}"]
        stack=[]
        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if len(stack) !=0 and stack[-1] == opened[closed.index(c)]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
    
    def isValid(self,s:str)->bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
            else:
                return False
        return len(stack) == 0 # 3
                
            
Solution()