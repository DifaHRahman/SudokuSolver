"""
Read/Write Sudoku Module
13518098
- Reads Sudoku from a text file ../test/ folder
- Writes Sudoku to a text file in ../result/ folder
- (WIP) Reads Sudoku from an image file in ../test/ folder
"""
import os.path
import sudoku

def readTxt(filename):
    result = sudoku.SudokuBoard()
    success = False
    try:
        print('Reading ../test/' + filename + '.txt')
        f = open('..\\test\\' + filename + '.txt')
        for i, line in enumerate(f):
            line = line.rstrip('\n')
            j = 0
            for c in line:
                if c != ' ':
                    if c == '#':
                        result.setSlot(i, j, '#')
                    elif int(c) > 0 or int(c)<=9:
                        result.setSlot(i, j, int(c))
                    else:
                        result.setSlot(i, j, 'X')
                    j+=1
        success = True
        print('File reading completed.')
        f.close()
                        
    except FileNotFoundError:
        print('File not found.')
    return result, success

def writeToTxt(filename, sudo):
    try:
        print('Menyimpan file ./test/' + filename + '.txt')
        f = open('..\\result\\' + filename + '.txt', 'w')
        for row in sudo:
            for column in row:
                f.write(str(column) + " ")
            f.write('\n')
        f.close()
        print("File saved.")
    except IOError:
        print("IOError. Unable to save.")