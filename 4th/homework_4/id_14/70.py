"""
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1, n2 = 1, 2
        for i in range(2, n):
            n1, n2 = n2, n1 + n2
        return n2

s = Solution()
ways = s.climbStairs(4)

print(ways)
