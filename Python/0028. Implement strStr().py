'''
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

'''



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1 - l2+1):
            if haystack[i:i+l2] == needle: return i
        return -1
    
    
print(Solution().strStr("noodle","le"))