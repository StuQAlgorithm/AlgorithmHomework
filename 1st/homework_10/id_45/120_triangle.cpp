class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();

        if (n == 0)
            return 0;

        if (n == 1)
            return triangle[0][0];

        vector<int> cur_min_sum = triangle[n - 1]; 
        for (int i = n - 2; i >= 0; --i) {
            for (int j = 0; j < triangle[i].size(); ++j) {
                cur_min_sum[j] = triangle[i][j] + min(cur_min_sum[j], cur_min_sum[j+1]);
            }
        }   
        return cur_min_sum[0];
    }
};
