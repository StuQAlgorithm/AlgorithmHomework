class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        if not triangle: return 0

        n = len(triangle)
        for i in range(n, 0, -1):
            for j in range(len(triangle[i - 1])):
                if i == n:
                    triangle[i - 1][j] = triangle[i - 1][j]
                else:
                    triangle[i - 1][j] = triangle[i - 1][j] + min(triangle[i][j], triangle[i][j + 1])

        return triangle[0][0]