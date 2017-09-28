# https://leetcode.com/problems/climbing-stairs/description/
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.
# dp[n] = dp[n-1] + dp[n-2]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        dp = [0 for _ in range(n+1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    for i in range(10):
        print(sol.climbStairs(i))
