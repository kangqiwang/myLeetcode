'''

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

'''

from typing import List


class Solution:        
   
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [["."]*n]*n
        board= [["."] * n for _ in range(n)]
        res=[]
        visited_cols= set()
        visited_diagonals=set()
        visited_antidiagonals=set()
        print(board)
        # print(state)
        def fillBoard(row):
            # print("row: "+str(row))
            # print("len(board): "+str(len(board)))
            if row == len(board): 
                res.append(["".join(row) for row in board])
                print("print board")
                print(board)
                return
            for i in range(len(board)):
                diff= row-i
                _sum=row+i
                if not (i in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):
                    visited_cols.add(i)
                    visited_diagonals.add(diff)
                    visited_antidiagonals.add(_sum)
                    board[row][i]="Q"
                    fillBoard(row+1)
                    visited_cols.remove(i)
                    visited_diagonals.remove(diff)
                    visited_antidiagonals.remove(_sum)
                    board[row][i]="."
            
        fillBoard(0)
        return res

print(Solution().solveNQueens(4))