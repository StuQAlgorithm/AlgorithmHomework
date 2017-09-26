class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ret = new ArrayList<>();

        Arrays.sort(nums);

        if(nums == null || nums.length < 4){
            return ret;
        }

        NSum(4, nums, target, 0, ret, new ArrayList<Integer>(4));

        return ret;
    }

    public static void NSum(int N,
                            int[] nums,
                            int target,
                            int left,
                            List<List<Integer>>ret,
                            List<Integer> preList){
        int n = nums.length;

        if(N*nums[left] > target || N*nums[n-1] < target){
            return;
        }

        if(N == 2){
            TwoSum(nums, target, left, ret, preList);
            return;
        }

        for(int i = left; i < n - N + 1; i++){
            if(i == left || (i > left && nums[i] != nums[i-1])){
                List<Integer> list = new ArrayList<Integer>(preList);
                list.add(nums[i]);
                NSum(N-1, nums, target - nums[i], i+1, ret, list);
            }
        }

    }

    public static void TwoSum(int[] nums,
                              int target,
                              int left,
                              List<List<Integer>>ret,
                              List<Integer> preList){
        int n = nums.length;
        int l = left;
        int r = n - 1;

        while(l < r){
            if(nums[l] + nums[r] == target){
                List<Integer> list = new ArrayList<Integer>(preList);
                list.add(nums[l]);
                list.add(nums[r]);
                ret.add(list);

                l++;
                r--;

                while(l < r && nums[l-1] == nums[l]) l++;
                while(l < r && nums[r+1] == nums[r]) r--;
            }else if(nums[l] + nums[r] > target){
                r--;
            }else{
                l++;
            }
        }

    }

}