'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

DP problem, use search from middle to slove, get function if palindromic

https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-5-longest-palindromic-substring/

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        head=""
        tail=""
        dic={}
        res = 0
        
            