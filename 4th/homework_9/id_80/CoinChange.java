

class Solution {
   
    private HashMap<Integer, Integer> map = new HashMap<>();
    public int coinChange(int[] coins, int amount) {
        
        // 刷硬币的问题
        //用多少次硬币能解决问题。
        // 解决问题的标志是什么？--》 关键得找出这个状态转移方程来。
        
        // 想不出来，超时了，看答案。
        
        //递归往回找。 StackOverFlow了。。
       
        
        // 说实话想不通。
        // 看代码都有点看不懂。。
        
        // 多看了几遍答案，现在来自己手写。
        if(amount == 0) {
            return 0;
        }
        if(map.get(amount) != null){
            return map.get(amount);
        }
        
        int min = Integer.MAX_VALUE;  // 其实只要比amount大就可以了。
        for (int coin : coins) {
            int current = 0;
            if (amount >= coin) {
                int next = coinChange(coins, amount - coin);
                if(next >=0) {
                    current = next + 1;
                }
            }
            
            if(current > 0) {
                //说明至少找到了。要去找最小的了。
                min = Math.min(min, current);
            }
        }
        
        int finalCount = (min==Integer.MAX_VALUE) ? -1 : min;
        map.put(amount,finalCount);
        return finalCount;
}
}
