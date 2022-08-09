'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


'''

from random import randrange
from typing import List
import numpy as np

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board,0,0)
    def solve(self,board,r,c) -> bool:
        while board[r][c]!=".":
            c+=1
            if c==9:c,r=0,r+1
            if r ==9: return True
        for i in range(1,10):
            if self.isValidSudokuMove(board,r,c,str(i)):
                board[r][c]=str(i)
                if self.solve(board,r,c):
                    return True
        board[r][c]="."
        return False
    
    def isValidSudokuMove(board,r,c,value):
        if any(board[r][i] == value for i in range(9)): return False
        if any(board[i][c] == value for i in range(9)): return False
        br,bc= 3*(r//3),3*(c//3)
        if any(board[i][j] == value for i in range(br,br+3) for j in range(bc,bc+3)):return False
        
        
    
        
    #     for r in board:
    #         for c in board:
    #             mlist= 
    #             for i in range(1,9):
    #                 if possible(board,c,r,i):
    #                     drawBoard(board,c,r,i)
    
    # def possibleValue(board,c,r):
    #     mlist= []
    #     board[:c]+board[r]
    
    # def possible(board,c,r,i):
    #     if i in board[c] or 
            
        
    #     print(np.matrix(board))
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
        
        
print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))