#!/usr/bin/python3
'''The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. '''
import sys
'''
#1 start from the leftmost column
#2 if all queens are placed, return.
#3 try all rows in the current column
# do following for every tried row.
# a. check if the queen can be placed safely
# and mark the cell, then check if this can lead to a solution
# b. if yes, return true
#c. else, unmarked the cell and goto #a.
# if all rows have been tried and nothing worked, return false
# to triggerd backtracking

# [0,1]

'''
if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """
    Places N non-attacking queens on an NxN chessboard.
    """
    col, pos, neg = set(), set(), set()
    current_board = [[] for n in range(n)]
    solved_board = []

    def backtrack(row):
        """
        Tool for solving constraint satisfaction problems.
        """
        if row == n:
            copy = current_board.copy()
            solved_board.append(copy)
            return

        for c in range(n):
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            current_board[row] = [row, c]

            backtrack(row + 1)

            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            current_board[row] = []

    backtrack(0)

    return solved_board


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)
