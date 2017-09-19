//if window size is small, this is faster, beacuse the biggest cost is the search in the window
//if window size is big, i think priorityQueue is faster, but use more space

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || nums.length < k) return new double[0];

        int n = nums.length;
        double[] ret = new double[n - k + 1];
        double[] windowArr = new double[k];

        for(int i = 0; i < k; i++){
            windowArr[i] = (double)nums[i];
        }

        Arrays.sort(windowArr);

        int kLeftMid = (k-1)/2;
        int kRightMid = k/2;

        for(int i = 0; i < ret.length; i++){
            if(i > 0){
                double outVal = nums[i - 1];
                double inVal = nums[i - 1 + k];
                slidingWindow(windowArr, outVal, inVal);
            }

            ret[i] = (windowArr[kLeftMid] + windowArr[kRightMid]) / 2d;
        }

        return ret;
    }

    public void slidingWindow(double[] windowArr, double outVal, double inVal){
        int n = windowArr.length;
        int removeIdx = Arrays.binarySearch(windowArr, outVal);

        while(removeIdx+1 <= n-1 && inVal > windowArr[removeIdx+1]) windowArr[removeIdx++] = windowArr[removeIdx];
        while(removeIdx-1 >= 0 && inVal < windowArr[removeIdx-1]) windowArr[removeIdx--] = windowArr[removeIdx];

        windowArr[removeIdx] = inVal;
    }
}


class Solution2 {
    PriorityQueue<Integer> leftPQ = new PriorityQueue<Integer>();
    PriorityQueue<Integer> rightPQ = new PriorityQueue<Integer>(Collections.reverseOrder());

    public double[] medianSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0 || nums.length < k) return new double[0];

        int n = nums.length;
        double[] ret = new double[n - k + 1];

        for(int i = 0; i < k; i++){
            add(nums[i]);
        }
        ret[0] = getMedian();

        for(int i = k; i < nums.length; i++){
            add(nums[i]);
            remove(nums[i - k]);
            ret[i - k + 1] = getMedian();
        }

        return ret;
    }

    public void add(int num){
        double median = getMedian();
        if(num > median){
            leftPQ.add(num);
        }else{
            rightPQ.add(num);
        }

        balance();
    }

    public void remove(int num){
        if(leftPQ.contains(num)){
            leftPQ.remove(num);
        }else{
            rightPQ.remove(num);
        }

        balance();
    }

    public void balance(){
        while(leftPQ.size() > rightPQ.size() + 1){
            rightPQ.add(leftPQ.poll());
        }
        while(rightPQ.size() > leftPQ.size() + 1){
            leftPQ.add(rightPQ.poll());
        }
    }

    public double getMedian(){
        if(leftPQ.size() == 0 && rightPQ.size() == 0){
            return 0;
        }

        if(leftPQ.size() > rightPQ.size()){
            return leftPQ.peek();
        }else if(leftPQ.size() < rightPQ.size()){
            return rightPQ.peek();
        }else{
            return ((long)leftPQ.peek() + (long)rightPQ.peek()) / 2d;
        }
    }


}