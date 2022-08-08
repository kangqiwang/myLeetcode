'''

Problem:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note: Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.



'''
from collections import Counter
from pickletools import read_unicodestring1

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        odd = False
        res = 0
        for key,value in counts.items():
            if value %2 ==0:
                res+=value
            else:
                res+=value-1
                odd=True
        if odd:
            res =res+1
        return res
print(Solution().longestPalindrome("abccccdd"))