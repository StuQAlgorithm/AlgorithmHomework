class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0) return 0;

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

        for(int i = 0; i < nums.length; i++){
            pq.add(nums[i]);
        }

        int longestLen = 1;
        int lastTempVal = pq.poll();
        int currentLen = 1;

        while(pq.size() > 0){
            int tempVal = pq.poll();

            if(lastTempVal+1 == tempVal){
                currentLen++;
                longestLen = Math.max(longestLen, currentLen);
            }else if(lastTempVal == tempVal){
                continue;
            }else{
                currentLen = 1;
                longestLen = Math.max(longestLen, currentLen);
            }

            lastTempVal = tempVal;
        }

        return longestLen;
    }
}