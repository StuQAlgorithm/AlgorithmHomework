
class Solution {
    public int rob(int[] nums) {
        
        // 直接拿1 的答案过来套， 因为有了环，所以要么终点往前移一个，要么起点往后移一个。
        //
        
        if(nums == null || nums.length ==0) {
            return 0;
        }
        if(nums.length == 1){
            return nums[0];
        }
        if(nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        
        
        
        int max[] = new int[nums.length-1];
        int max2[] = new int[nums.length -1];
    
        for(int i=0; i<nums.length -1; i++) {
            if (i==0) {
                max[0] = nums[0];
                continue;
            } 
            if(i ==1) {
                max[1] = Math.max(nums[0], nums[1]); 
                continue;
            }
            max[i] = Math.max(max[i-2] +nums[i], max[i-1]);
        }
        
        for(int i=1; i<nums.length ; i++) {
            if (i==1) {
                max2[0] = nums[1];
                continue;
            } 
            if(i ==2) {
                max2[1] = Math.max(nums[1], nums[2]); 
                continue;
            }
            max2[i-1] = Math.max(max2[i-3] +nums[i], max2[i-2]);
        }
        
        return Math.max(max[max.length -1], max2[max.length-1]);
        
        
        
    
        
    }
}
