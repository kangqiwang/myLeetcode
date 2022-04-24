from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        print(grid)
        visit, curr = set(), collections.deque()
		# find all fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        
        result = 0
        while visit and curr:
            print("this is the visit")
            print(visit)
            print("this is curr")
            print(curr)
			# BFS iteration
            for _ in range(len(curr)):
                i, j = curr.popleft()  # obtain recent rotten orange
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit:  # check if adjacent orange is fresh
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
		# check if fresh oranges remain and return accordingly
        return -1 if visit else result


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))