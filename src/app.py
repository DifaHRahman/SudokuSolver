"""
Main program of SudokuSolver
13518098
"""

import sudoku, util

# Util test
fname = input("Masukan nama file txt: ")
game, comp = util.readTxt(fname)
game.show()
print("Solving Sudoku...")

if game.solveBoard(0, 0):
    print("Hasil:")
    game.show()
    sname = input("Masukan nama file save txt: ")
    util.writeToTxt(sname, game.getBoard())
else:
    print("Unable to complete.")
