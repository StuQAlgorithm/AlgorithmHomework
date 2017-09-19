"""
01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0
for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

from collections import deque
import sys
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = sys.maxsize

        while queue:
            i, j = queue.popleft()
            # 设置临近点
            for dx, dy in zip((1, -1, 0, 0), (0, 0, 1, -1)):
                ny = i + dy
                nx = j + dx

                if ny < 0 or ny >= m or nx < 0 or nx >= n:
                    continue
                value = matrix[ny][nx]
                if value <= matrix[i][j] + 1: # 更新过, 且更小(近)
                    continue
                # 加入队列继续处理
                queue.append((ny, nx))
                # 更新, 临近点 + 1
                matrix[ny][nx] = matrix[i][j] + 1
        return matrix



# matrix = [
#     [0],
#     [0],
#     [0],
#     [0],
#     [0]
# ]
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
s = Solution()
list = s.updateMatrix(matrix)
print(list)




