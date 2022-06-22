'''

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(collections.Counter(ransomNote))
        print(collections.Counter(magazine))
        print( collections.Counter(ransomNote)-collections.Counter(magazine))
        
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
    
print(Solution().canConstruct("aaa","ba"))