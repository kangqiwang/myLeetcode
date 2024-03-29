'''
There is a robot on an m x n grid. The robot is initially 
located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner
(i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, 
return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:


Input: m = 3, n = 7
Output: 28


Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


'''

# f(x,y) = f(x-1,y) + f(x,y-1)
# f(0,0) = 1
# dp[r][c] = dp[r][c]+dp[r-1][c]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r][c-1]+dp[r-1][c]
        print(dp)
        return dp[m-1][n-1]
        
        
if __name__ == '__main__':
    m = 3
    n = 3
    print(Solution().uniquePaths(m,n))