/**
 * https://leetcode.com/problems/3sum/description/
 */
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> ret = new ArrayList<>();
        int n = nums.length;

        for(int i = 0; i < n; i++){
            if(i == 0 || (i>0 && nums[i-1] != nums[i])){
                int left = i + 1;
                int right = n - 1;
                int target = -nums[i];

                while(left < right){
                    if(nums[left] + nums[right] == target){
                        ret.add( Arrays.asList(nums[i], nums[left], nums[right]) );
                        left++;
                        right--;
                        while(left < right && nums[left] == nums[left-1]) left++;
                        while(left < right && nums[right] == nums[right+1]) right--;
                    }else if(nums[left] + nums[right] > target){
                        right--;
                    }else{
                        left++;
                    }


                }

            }
        }

        return ret;
    }
}