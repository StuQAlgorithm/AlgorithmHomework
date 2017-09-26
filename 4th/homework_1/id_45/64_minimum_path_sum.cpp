class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> result;
        for (int i = 0; i < n; ++i) {
            vector<int> vec(m, -1);
            result.push_back(vec);
        }
        findMinPathSum(grid, n - 1, m - 1, result); 
        return result[n-1][m-1];
    }
    int findMinPathSum(vector<vector<int>>& grid, int i, int j, vector<vector<int>>& result) {
        if (i < 0 || j < 0)
            return INT_MAX;
        if (result[i][j] != -1)
            return result[i][j];
        if (i == 0 && j == 0)
            return result[i][j] = grid[i][j];
        return result[i][j] = grid[i][j] + min(findMinPathSum(grid, i - 1, j, result), findMinPathSum(grid, i, j - 1, result));
    }
};
