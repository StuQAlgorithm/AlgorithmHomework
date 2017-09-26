class Solution {
    public void sortColors(int[] nums) {
        int len = nums.length;
        int left = 0;
        int right = len - 1;

        for(int i = left; i <= right; i++){
            while(nums[i] == 2 && i < right) swap(nums, i, right--);
            while(nums[i] == 0 && i > left) swap(nums, i, left++);
        }
    }

    public void swap(int[] nums, int a, int b){
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}