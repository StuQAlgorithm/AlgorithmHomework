//unordered_set find element: O(1), because of using hash
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        unordered_set<int> unoset(nums.begin(), nums.end());

        int result = 0;
        int left_ele, right_ele;
        for (int i = 0; i < nums.size(); ++i) {
            if (unoset.find(nums[i]) != unoset.end()) {
                unoset.erase(nums[i]);
                left_ele = nums[i] - 1;
                right_ele = nums[i] + 1;
                while (unoset.find(left_ele) != unoset.end()) {
                    unoset.erase(left_ele);
                    --left_ele;
                }

                while (unoset.find(right_ele) != unoset.end()) {
                    unoset.erase(right_ele);
                    ++right_ele;
                }
                if (result < right_ele - left_ele - 1)
                    result = right_ele - left_ele - 1;
            }
        }
        return result;
    }
};
