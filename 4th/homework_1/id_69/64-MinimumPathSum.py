# https://leetcode.com/problems/minimum-path-sum/description/
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# dp[i][j] i: 0->len(grid)-1 j: 0->len(grid[1])-1
# dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or grid == []: return
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)-1, -1, -1):
                for j in range(len(grid[0])-1, -1, -1):
                    dp[i][j] = grid[i][j]
                    if i == len(grid) -1 and j == len(grid[0])-1:
                        continue
                    elif i + 1 >= len(grid):
                        dp[i][j] += dp[i][j+1]
                    elif j + 1 >= len(grid[0]):
                        dp[i][j] += dp[i+1][j]
                    else:
                        dp[i][j] += min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

# 状态压缩
# class Solution(object):
#     def minPathSum(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         sum = list(grid[0])
#         for j in range(1, len(grid[0])):
#             sum[j] = sum[j - 1] + grid[0][j]
#         for i in range(1, len(grid)):
#             sum[0] += grid[i][0]
#             for j in range(1,len(grid[0])):
#                 sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]
#         return sum[-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.minPathSum([[0,9],[1,2]]))
