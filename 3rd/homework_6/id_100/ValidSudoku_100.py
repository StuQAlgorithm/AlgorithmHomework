class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if not board:
            return False

        m, n = len(board), len(board[0])
        check_row = [[0 for i in range(9)] for j in range(9)]
        check_col = [[0 for i in range(9)] for j in range(9)]
        check_box = [[0 for i in range(9)] for j in range(9)]

        for i in range(m):
            for j in range(n):
                if not board[i][j] == '.':
                    num = int(board[i][j]) - 1
                    k = i / 3 * 3 + j / 3  # ??
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False

                    check_row[i][num] = check_col[j][num] = check_box[k][num] = 1

        return True
