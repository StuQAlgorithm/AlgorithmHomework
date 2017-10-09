
class Solution {
    public int rob(int[] nums) {
        
        // 题意是还算简单易懂，但是怎么个做法了。
        
        // 求max。
        
        // 直接遍历，按单双数是有问题的。
        
        //其实是不是只有四种情况，以1或2为起点，然后3/4和 4/5变成了可以选择的选项？
        //求出最大值，一直更新最大值即可。
        //这个算dfs吧
        
        // 那dp了？想不出来dp有什么招啊！ dfs肯定又超时。
        
        //最后两家肯定抢一家。
        // 好了，只想出了low的dfs.
        if(nums == null || nums.length ==0) {
            return 0;
        }
        
    // 有个关系在这。
        for(int i=0; i<nums.length; i++) {
            if (i==0) {
                continue;
            } 
            if(i ==1) {
                nums[1] = Math.max(nums[0], nums[1]); 
                continue;
            }
            nums[i] = Math.max(nums[i-2] +nums[i], nums[i-1]);
        }
        
        return nums[nums.length -1];
    }
}
