class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;
        int result = nums[0];
        int curMax = nums[0];
        int curMin = nums[0];
        int preMax;

        for (int i = 1; i < n; ++i) {
            preMax = curMax;
            curMax = max(max(curMax * nums[i], curMin * nums[i]), nums[i]);
            curMin = min(min(preMax * nums[i], curMin * nums[i]), nums[i]);
            result = max(result, curMax);
        }
        return result;
    }
};
