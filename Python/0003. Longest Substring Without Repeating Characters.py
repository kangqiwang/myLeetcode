'''

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''




from itertools import count
from tkinter.tix import LabelEntry
from turtle import left

from pandas import set_eng_float_format


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        first = -1
        output = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>first:
                first =seen[s[i]]
            seen[s[i]]=i
            output = max(output,i-first)
        return output
    def lengthOfLongestSubstring2(self, s: str) -> int:
        seen={}
        left = 0
        output = 0
        for i in range(len(s)):
            if s[i] not in seen:
                output=max(output,i-left+1)
            else:
                if seen[s[i]] <1:
                    output=max(output,i-left+1)
                else:
                    left = seen[s[i]]+1
        return output
    def lengthOfLongestSubstring3(self, s:str) -> int:
        seen={}
        first = 0
        output=0
        for i in range(len(s)):
            if s[i] in seen:
                first = seen[s[i]]
            else:
                output = max(output,i-first+1)
            seen[s[i]]=i
        return output
print(Solution().lengthOfLongestSubstring3("abcabcbb"))
            
            
        