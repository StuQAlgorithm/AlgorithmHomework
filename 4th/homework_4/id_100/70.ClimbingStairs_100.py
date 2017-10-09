class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        
        return res[n - 1]