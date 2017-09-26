//test case
/*
[[1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1]]

 //test case
 [[3],
  [2]]

 //ans
 [3,2]

 //test case
 [[3,2]]

 //ans
 [3,2]
*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int m = matrix.size();
        if (m > 0) {
            int n = matrix[0].size();
            int r_top_left = 0, c_top_left = 0;
            int r_bottom_right = m - 1, c_bottom_right = n - 1;

            while ((r_top_left <= r_bottom_right) && (c_top_left <= c_bottom_right)) {
                int s, e;
                //-->
                s = c_top_left;
                e = c_bottom_right + 1;
                while (s < e) {
                    result.push_back(matrix[r_top_left][s]);
                    ++s;
                }

                //right side down
                s = r_top_left + 1;
                e = r_bottom_right + 1;
                while (s < e) {
                    result.push_back(matrix[s][c_bottom_right]);
                    ++s;
                }

                //<--
                if (r_top_left != r_bottom_right) { //Attention
                    s = c_bottom_right - 1;
                    e = c_top_left;
                    while (s > e) {
                        result.push_back(matrix[r_bottom_right][s]);
                        --s;
                    }
                }

                //left side up
                if (c_top_left != c_bottom_right) { // Attention
                    s = r_bottom_right;
                    e = r_top_left;
                    while (s > e) {
                        result.push_back(matrix[s][c_top_left]);
                        --s;
                    }
                }

                ++r_top_left;
                ++c_top_left;
                --r_bottom_right;
                --c_bottom_right;
            }
        }
        return result;
    }
};
