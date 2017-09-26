
class Solution {
    public int maxProfit(int[] prices) {
        // 没思路 啊?
        // 多次买入卖出。
        
        // 只能dp吧？贪心估计算出来不是全局最优。
        //可以考虑，以每个节点为买入点，一直遍历到结尾，求出其所有可能的卖出点。但是这样是单次的吧，第二次买入点了？
        // 想不出来，看答案了。
        
        // 艹尼玛！！！看了答案，好简单啊！！！
        
        int total = 0;
    for (int i=0; i< prices.length-1; i++) {
        if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
    }
    
    return total;
    }
}
