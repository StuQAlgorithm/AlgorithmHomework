class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        vector<vector<int>> result;
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return result;

        int n = matrix.size();
        int m = matrix[0].size();
        int distance;

        for (int i = 0; i < n; ++i) {
            vector<int> vec;
            for (int j = 0; j < m; ++j) {
                distance = 0;  
                if (matrix[i][j] != 0) {
                    distance = calDistance(i, j, matrix);
                }
                vec.push_back(distance);
            }
            result.push_back(vec);
        }
        return result;
    }
    int calDistance(int i, int j, vector<vector<int>>& matrix) {
        queue<pair<int, int>> qu; 
        pair<int, int> cord;
        int size, dis = 0;
        int n = matrix.size();
        int m = matrix[0].size();

        qu.push(make_pair(i, j));
        while (!qu.empty()) {
            size = qu.size();
            for (int k = 0; k < size; ++k) {
                cord = qu.front();
                qu.pop();
                i = cord.first;
                j = cord.second;
                if (i - 1 >= 0) {
                    if (matrix[i-1][j] == 0)
                        return dis + 1;
                    else
                        qu.push(make_pair(i-1, j));
                }
                if (i + 1 < n) {
                    if (matrix[i+1][j] == 0)
                        return dis + 1;
                    else
                        qu.push(make_pair(i+1, j));
                }
                if (j - 1 >= 0) {
                    if (matrix[i][j-1] == 0)
                        return dis + 1;
                    else
                        qu.push(make_pair(i, j-1));
                }
                if (j + 1 < m) {
                    if (matrix[i][j+1] == 0)
                        return dis + 1;
                    else
                        qu.push(make_pair(i, j+1));
                }
            }
            ++dis;
        }
        return dis;
    }   
};
