# author: lu19kend
# https://leetcode.com/problems/spiral-matrix/description/


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix is None:
            return matrix
        width = len(matrix[0])
        depth = len(matrix)
        plus = 1
        x, y = 0, 0
        res = []
        while(width > 0 and depth > 0):
            for i in range(width):
                res.append(matrix[x][y])
                matrix[x][y] = True
                if i != width - 1:
                    y += plus
            x += plus
            for j in range(depth - 1):
                res.append(matrix[x][y])
                matrix[x][y] = True
                if j != depth - 2:
                    x += plus
            plus = - plus
            y += plus
            width -= 1
            depth -= 1
        return res
