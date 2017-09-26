
class Solution {
    public int maxProduct(int[] nums) {
        
        //1. 求乘积. 0也可以考虑进去的，关键要考虑负数的问题。 --》 忘了。还要是相邻的。
        //2. dfs怎么搞？
        // dp又怎么搞？ 如何找到要递推的东西？
        
        //想不出来。 负数的位置让我找不出任何规律。
        
        //看答案。
        
        
        int r = nums[0];
        int n = nums.length;
    // imax/imin stores the max/min product of
    // subarray that ends with the current number A[i]
    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (nums[i] < 0) {
            int temp = imin;
            imin = imax;
            imax = temp;
        }
            

        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = Math.max(nums[i], imax * nums[i]);
        imin = Math.min(nums[i], imin * nums[i]);

        // the newly computed max value is a candidate for our global result
        r = Math.max(r, imax);
    }
    return r;
        
        
        
        
    }
}
