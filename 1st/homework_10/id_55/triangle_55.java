class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle == null || triangle.size() == 0) return 0;

        int n = triangle.size();
        int[] min = new int[triangle.get(n - 1).size() + 1]; //as add one layer to the bottom

        for(int i = n - 1; i >= 0; i--){
            for(int j = 0; j < triangle.get(i).size(); j++){
                min[j] = triangle.get(i).get(j) + Math.min(min[j], min[j + 1]);
            }
        }

        return min[0];
    }
}