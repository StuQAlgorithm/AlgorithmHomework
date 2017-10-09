class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int robCurHouse = 0;
        int notRobCurHouse = 0;
        for (int i = 0; i < n; ++i) {
            int robPreHouse = robCurHouse;
            int notRobPreHouse = notRobCurHouse;
            robCurHouse = nums[i] + notRobPreHouse;
            notRobCurHouse = max(robPreHouse, notRobPreHouse);
        }
        return max(robCurHouse, notRobCurHouse);
    }
};
