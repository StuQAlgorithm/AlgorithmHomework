#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int l, r, c, d, two_sum;
        vector<vector<int> >result;
        sort(nums.begin(), nums.end());

        for (int k = 0; k < nums.size();) {
            d = nums[k];
            for (int i = k + 1; i < nums.size();) {
                c = nums[i];
                l = i + 1;
                r = nums.size() - 1;

                while (l < r) {
                    two_sum = nums[l] + nums[r];
                    if (two_sum > target - c - d) {
                        --r;
                    } else if(two_sum < target - c - d) {
                        ++l;
                    } else {
                        vector<int> vec;
                        vec.push_back(d);
                        vec.push_back(c);
                        vec.push_back(nums[l]);
                        vec.push_back(nums[r]);
                        result.push_back(vec);

                        int l_val = nums[l];
                        ++l;
                        while (l < r) {
                            if (l_val == nums[l]) {
                                ++l;
                            } else {
                                break;
                            }
                        }

                        int r_val = nums[r];
                        --r;
                        while (l < r) {
                            if (r_val == nums[r]) {
                                --r;
                            } else {
                                break;
                            }
                        }
                    }
                }
                ++i;
                while (i < nums.size()) {
                    if (c == nums[i]) {
                        ++i;
                    } else {
                        break;
                    }
                }
            }
            ++k;
            while (k < nums.size()) {
                if (d == nums[k]) {
                    ++k;
                } else {
                    break;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution test_solution = Solution();
    int target = 0;
    int t_array[] = {1, 0, -1, 0, -2, 2};
    vector<int> t_vec(t_array, t_array + sizeof(t_array) / sizeof(int));
    test_solution.fourSum(t_vec, target);
    return 0;
}
