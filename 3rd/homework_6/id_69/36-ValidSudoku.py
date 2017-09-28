# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
       	for r in len(board):
       		  for c in len(board[0]):
       		  		if board[r][c] == '.': continue
       		  	  res = self.dfs(board, r, c, board[r][c])

    def dfs(self, board, r, c, n):
