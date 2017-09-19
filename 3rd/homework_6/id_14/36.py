"""
Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #
        if not board:
            return True

        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        subGrid = [[] for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                if cell != ".":
                    leftTop = i / 3 * 3 + j / 3
                    if cell in row[i] or cell in col[j] or cell in subGrid[leftTop]:
                        return False
                    row[i].append(cell)
                    col[j].append(cell)
                    subGrid[leftTop].append(cell)
        return True



