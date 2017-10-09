//Solution 1: one pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;
        for (int i = 0; i <= r; ++i) {
            if (i == r) {
                if (nums[i] != 0) {
                    break;
                }
            }
            if (nums[i] == 0) {
                if (l < i) {
                    int t = nums[i];
                    nums[i] = nums[l];
                    nums[l] = t;
                }
                ++l;

            } else if (nums[i] == 2) {
                int t = nums[i];
                nums[i] = nums[r];
                nums[r] = t;
                --r;
                --i;
            }
        }
    }
};

//Solution 2: two pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int color_cnt[3] = {0, 0, 0};
        for (int i = 0; i < nums.size(); ++i) {
            ++color_cnt[nums[i] % 3];
        }
        int k = 0;
        for (int i = 0; i < 3; ++i) {
            while (color_cnt[i]--) {
                nums[k++] = i;
            }
        }
    }
};
