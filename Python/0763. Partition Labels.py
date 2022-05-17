"""

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.


"""


from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i,c in enumerate(S)}
        print(last)
        start = end = 0
        output = []
        for i,c in enumerate(S):
            end = max(end,last[c])
            if i == end:
                print(c)
                print(end)
                print(start)
                output.append(end-start+1)
                start = i + 1
        return output

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
