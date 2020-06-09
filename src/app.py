"""
Main program of SudokuSolver
"""

import sudoku, util

# Util test
fname = input("Masukan nama file txt: ")
game, comp = util.readTxt(fname)
game.show()

sname = input("Masukan nama file save txt: ")
util.writeToTxt(sname, game.getBoard())
