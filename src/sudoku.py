"""
Sudoku Class Object
"""

class SudokuBoard:
    def __init__(self):
        self.N = 9
        self.board = [[0 for i in range(9)] for j in range(9)] # 0 means none

    def setSlot(self, i, j, num):
        self.board[i][j] = num

    def getSlot(self, i, j):
        return self.board[i][j]
    
    def getBoard(self):
        return self.board

    def getN(self):
        return self.N
        
    def show(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    print('#', end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()