"""
Sudoku Class Object
13518098
"""

# X for unknown value.
# 0 or # for unassigned value.
class SudokuBoard:
    def __init__(self):
        '''Default ctor.'''
        self.board = [[0 for i in range(9)] for j in range(9)] # 0 means none

    def setSlot(self, i, j, num):
        ''' Slot setter. '''
        self.board[i][j] = num

    def getSlot(self, i, j):
        ''' Slot getter. '''
        return self.board[i][j]
    
    def getBoard(self):
        ''' Board getter. '''
        return self.board

    def isKnown(self):
        ''' Returns true if Sudoku data is complete
         (no unknown value).'''
        result = True
        for i in self.board:
            if 'X' in i:
                result = False
                break
        return result

    def isUsedinBox(self, num, i, j):
        row = (i // 3)*3
        col = (j // 3)*3
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == num:
                    return True
        return False

    def isUsedinCol(self, num, j):
        for r in range(9):
            if self.board[r][j] == num:
                return True
        return False

    def isUsedinRow(self, num, i):
        for c in range(9):
            if self.board[i][c] == num:
                return True
        return False

    def isEmpty(self, i, j):
        return self.board[i][j] == '#'

    def isAbleToFillWith(self, num, i, j):
        if not (self.isUsedinBox(num, i, j) or self.isUsedinCol(num, j) or self.isUsedinRow(num, i)):
            return True
        return False

    def isCompleted(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '#':
                    return False
        return True

    def solveBoard(self, i, j):
        '''Solver method'''
        if self.isCompleted():
            return True

        if self.isEmpty(i, j):
            for num in range(1, 10):
                if self.isAbleToFillWith(num, i, j):
                    self.setSlot(i, j, num)
                    r = i
                    c = j + 1
                    if c == 9:
                        c = 0
                        r += 1
                    if self.solveBoard(r, c):
                        return True
                    else:      
                        self.setSlot(i, j, '#')
        else:
            r = i
            c = j + 1
            if c == 9:
                c = 0
                r += 1
            return self.solveBoard(r, c)
        return False        

    def show(self):
        ''' Print board to terminal. '''
        for i in range(9):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print(self.board[i][8])