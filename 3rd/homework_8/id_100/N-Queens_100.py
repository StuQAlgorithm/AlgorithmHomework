class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        self.dfs(board, 0)
        return self.res

    def dfs(self, board, index):
        if index == len(board):
            self.res.append(self.construct(board))
            return

        for i in range(len(board)):
            if self.validate(board, i, index):
                board[i][index] = 'Q'
                self.dfs(board, index + 1)
                board[i][index] = '.'

    def validate(self, board, x, y):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Q' and (x + j == y + i or x + y == i + j or x == i):
                    return False
        return True

    def construct(self, board):
        ll = []
        for i in range(len(board)):
            ll.append(''.join(board[i]))
        return ll
