"""
 N-Queens

 The n-queens puzzle is the problem of placing n queens on an n×n chessboard
 such that no two queens attack each other.Given an integer n,
 return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution(object):
    def helper(self, n, diagonalA, diagonalB, queens, solutions):
        p = len(queens)
        if p == n:
            solutions.append(queens)
            return None

        for q in range(n):
            if q in queens or p - q in diagonalA or p + q in diagonalB:
                continue
            self.helper(n, diagonalA + [p - q], diagonalB + [p + q], queens + [q], solutions)


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solutions = []
        self.helper(n, [], [], [], solutions)
        results = []
        for solution in solutions:
            board = []
            for i in range(n):
                m = solution[i]
                str = ""
                for j in range(n):
                    str += "Q" if m == j else "."
                board.append(str)
            results.append(board)
        return results

s = Solution()
board = s.solveNQueens(4)
print(board)



