'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

'''


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
    
