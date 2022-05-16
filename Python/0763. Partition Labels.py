from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result,last_seen,max_last_seen,count =[],{},0,0
        for i, char in enumerate(s):
            last_seen[char] = i
        print(last_seen)
        
print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
