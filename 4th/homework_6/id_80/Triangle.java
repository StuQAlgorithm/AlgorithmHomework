
class Solution {
    
    public int minimumTotal(List<List<Integer>> triangle) {
    
        // dp
        // 从下至上，修改没一个值。
        if(triangle == null ||triangle.size() == 0) {
            return 0;
        }
        
        int len = triangle.size();
        
        for(int i=len - 2; i>=0; i--) {
            List<Integer> list = triangle.get(i);
            List<Integer> list2 = triangle.get(i+1);
            
            for(int j =0;j< list.size(); j++) {
                list.set(j, Math.min(list2.get(j), list2.get(j+1)) + list.get(j)); 
            }
            
        }
        return triangle.get(0).get(0);
        
        
    
    }
    
}


