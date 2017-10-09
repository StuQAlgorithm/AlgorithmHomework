class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int result = sum;
        for (int i = 1; i < nums.size(); ++i) {
            sum += nums[i];
            sum = sum < nums[i]? nums[i] : sum;
            result = result < sum? sum : result;
        }   
        return result;
    }
};
