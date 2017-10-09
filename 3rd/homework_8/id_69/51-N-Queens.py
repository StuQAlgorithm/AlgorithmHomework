# The n-queens puzzle is the problem of placing n queens
# on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution(object):
    def __init__(self):
        self.check_set = set() # 0: col, 1: dig(minus), 2:dig(plus)
        self.res = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.dfs(n, 0, [])
        return [[ '.'*i + 'Q' + '.'*(n-i-1) for i in r] for r in self.res]

    def dfs(self, n, row, cur_res):
        if row >= n:
            self.res.append(cur_res)
            return

        for i in range(n):
            if (0, i) in self.check_set or (1, row - i) in self.check_set or (2, row + i) in self.check_set:
                continue
            self.check_set.add((0, i))
            self.check_set.add((1, row-i))
            self.check_set.add((2, row+i))
            self.dfs(n, row + 1, cur_res + [i])
            self.check_set.remove((0, i))
            self.check_set.remove((1, row-i))
            self.check_set.remove((2, row+i))

# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         mask = (1 << n) - 1
#         st = {1 << i : '.' * (n - i - 1) + 'Q' + '.' * i for i in range(n)}
#         s = [0 for _ in xrange(n)]  # selection
#         p = [0 for _ in xrange(n)]  # not tried
#         x = [0 for _ in xrange(n)]  # sum (s[i]), up to down
#         y = [0 for _ in xrange(n)]  # sum (s[i] << n + ~i), right up to left down
#         z = [0 for _ in xrange(n)]  # sum (s[i] << i), left up to right down
#         res = []
#         i = 0
#         p[i] = mask
#         while i >= 0:
#             s[i] = p[i] & -p[i]
#             if s[i] == 0:
#                 i -= 1
#             else:
#                 p[i] &= ~s[i]
#                 if i == n - 1:
#                     res.append(map(lambda x: st[x], s))
#                 else:
#                     x[i + 1] = x[i] | s[i]
#                     y[i + 1] = y[i] | s[i] << n + ~i
#                     z[i + 1] = z[i] | s[i] << i
#                     i += 1
#                     p[i] = mask & ~(x[i] | y[i] >> n + ~i | z[i] >> i)
#         return res

if __name__ == '__main__':
    print(Solution().solveNQueens(4))



