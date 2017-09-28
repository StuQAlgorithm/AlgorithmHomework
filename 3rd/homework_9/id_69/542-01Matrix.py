# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.
# Example 1:
# Input:

# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:

# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[i][j] = self.bfs(i, j, matrix)
        return res

    def bfs(self, row, col, matrix):
        queue = []
        seen = set()
        queue.append((row, col))
        level_size = 1
        res = 0
        while queue:
            for _ in range(level_size):
                row, col = queue.pop(0)
                node = matrix[row][col]
                if node == 0: return res
                seen.add((row, col))
                if (row + 1, col) not in seen and row + 1 < len(matrix): queue.append((row+1, col))
                if (row - 1, col) not in seen and row - 1 >= 0: queue.append((row-1, col))
                if (row, col - 1) not in seen and col - 1 >= 0: queue.append((row, col-1))
                if (row, col + 1) not in seen and col + 1 < len(matrix[0]): queue.append((row, col+1))
            res += 1
            level_size = len(queue)

# dp
# class Solution {
# public:
#     vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#         int h=matrix.size(), w=matrix[0].size();
#         vector<vector<int>> dp(h,vector<int>(w,INT_MAX));
#         for(int times=0;times<=1;times++) // two passes, first forward then backward
#             for(int i=times?h-1:0;times?i>=0:i<h;times?i--:i++)
#                 for(int j=times?w-1:0;times?j>=0:j<w;times?j--:j++)
#                         if(matrix[i][j]==0)
#                             dp[i][j]=0;
#                         else {
#                             if(i&&dp[i-1][j]!=INT_MAX&&dp[i][j]>dp[i-1][j]+1) // look up
#                                 dp[i][j]=dp[i-1][j]+1;
#                             if(j&&dp[i][j-1]!=INT_MAX&&dp[i][j]>dp[i][j-1]+1) // look left
#                                 dp[i][j]=dp[i][j-1]+1;
#                             if(i<h-1&&dp[i+1][j]!=INT_MAX&&dp[i][j]>dp[i+1][j]+1) // look down
#                                 dp[i][j]=dp[i+1][j]+1;
#                             if(j<w-1&&dp[i][j+1]!=INT_MAX&&dp[i][j]>dp[i][j+1]+1) // look right
#                                 dp[i][j]=dp[i][j+1]+1;
#                         }
#         return dp;
#     }
# };



if __name__ == '__main__':
    print(Solution().updateMatrix([[0],[0],[0],[0],[0]]))




