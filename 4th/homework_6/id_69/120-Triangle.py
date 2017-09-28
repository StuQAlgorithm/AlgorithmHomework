# https://leetcode.com/problems/triangle/description/
# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.
# dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
from collections import deque
class Solution(object):
    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     if not triangle: return 0
    #     if len(triangle) < 2: return triangle[0][0]
    #     dp = []
    #     dp[:] = triangle
    #     for i in range(len(triangle)-2, -1, -1):
    #         for j in range(len(triangle[i])):
    #             dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
    #     return dp[0][0]

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        if len(triangle) < 2: return triangle[0][0]
        pre = triangle[-1]
        res = deque(pre)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                pre[j] = min(pre[j],pre[j+1]) + triangle[i][j]
            pre.pop()
            res.appendleft(pre)
        return res[0][0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))


