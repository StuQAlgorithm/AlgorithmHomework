"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time
"""

# dp
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid[0])
        n = len(grid)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                if i == n - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1]
                elif j == m - 1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]


# 递归 + cache
class Solution2(object):
    def __init__(self):
        self.cache = {}
    def helper(self, grid, i, j, m, n):
        if i == n - 1 and j == m - 1:
            return grid[i][j]

        key = str(i) + "_" + str(j)
        if key in self.cache:
            return self.cache[key]

        value = None
        if i == n - 1:
            value = grid[i][j] + self.helper(grid, i, j + 1, m, n)
        elif j == m - 1:
            value = grid[i][j] + self.helper(grid, i + 1, j, m, n)
        else:
            value = grid[i][j] + min(self.helper(grid, i + 1, j, m, n), self.helper(grid, i, j + 1, m, n))

        self.cache[key] = value

        return value

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid[0])
        n = len(grid)

        return self.helper(grid, 0, 0, m, n)

grid = [
    [1,2,5],
    [3,2,1]
]

s = Solution()
minSum = s.minPathSum(grid)
print(minSum)

