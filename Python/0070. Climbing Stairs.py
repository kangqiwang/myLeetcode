'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

input: n=0
output : 0

n=4
1*4
211
121
112
22
5

n=5
5*1
221
122
212
1112
1121
1211
2111
8

n=6
6*1
222
1122
1221
2112
2211
2121
1212

8

n=7
1*7
2221
1222
2122


'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
print(Solution().climbStairs(10))