

class Solution {
    

    public int climbStairs(int n) {
        
        // 一共n阶台阶
        // 每次一阶或者两阶
        // 共有几种方式完成攀登。
        
        // 感觉和生成括号有点类似。
        // dfs? --> 超时了。
        // 二分搜索后相乘？  --》应该是这个思路。 --->操蛋了。
        
        //根据test发现，其实是个fib数列。我曹了。 --> 原理是，到达最后一个节点的方法，只有两种，即从倒数第二个到达，和从倒数第三个到达
         
        if (n ==1) {
            return 1;
        } if(n == 2) {
            return 2;
        }
        int [] result = new int [n];
        result[0] =1;
        result[1]=2;
        
        for (int i=2; i<n ; i++) {
            result[i] = result[i-1]+result[i-2];
        }
        return result[n-1];
        
    }
    
    

    
}
