class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                else:
                    matrix[i][j] = 10000

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue != []:
            curr = queue[0]
            queue.remove(curr)
            for d in dirs:
                x = curr[0] + d[0]
                y = curr[1] + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or \
                        matrix[x][y] <= matrix[curr[0]][curr[1]] + 1:
                    continue
                queue.append([x, y])
                matrix[x][y] = matrix[curr[0]][curr[1]] + 1

        return matrix
