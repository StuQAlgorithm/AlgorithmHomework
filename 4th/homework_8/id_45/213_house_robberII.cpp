class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        if (nums.size() == 1)
            return nums[0];

        int result = 0;
        int robCurHouse, notRobCurHouse;
        int robPreHouse, notRobPreHouse;
        int start, end;
        for (int k = 0; k < 2; ++k) {
            if (k == 0) {
                start = 0; end = nums.size() - 1;
            } else {
                start = 1; end = nums.size();
            }
            robCurHouse = notRobCurHouse = 0;
            for (int i = start; i < end; ++i) {
                robPreHouse = robCurHouse;
                notRobPreHouse = notRobCurHouse;

                robCurHouse = nums[i] + notRobPreHouse;
                notRobCurHouse = max(robPreHouse, notRobPreHouse);
            }
            result = max(result, max(robCurHouse, notRobCurHouse));
        }
        return result;
    }
};
