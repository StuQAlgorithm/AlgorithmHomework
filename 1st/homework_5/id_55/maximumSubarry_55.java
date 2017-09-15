class Solution {
    public int maxSubArray(int[] nums) {
        int[] maxSubArr = new int[nums.length];
        maxSubArr[0] = nums[0];
        int max = nums[0];

        for(int i = 1; i< nums.length; i++){
            maxSubArr[i] = nums[i] + (maxSubArr[i-1] > 0 ? maxSubArr[i-1] : 0);
            max = Math.max(max, maxSubArr[i]);
        }

        return max;

    }
}