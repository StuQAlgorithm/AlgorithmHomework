
class Solution {
    public int minPathSum(int[][] grid) {
        // 比较典型的dp, 找最小。
        // 应该是需要dfs?全盘dfs吗？好像是需要额。
        // 方式一是dfs,全盘遍历，记录最小值。
        // 方式二是dp. 从最底层元素往回找，更新每个元素的值。最小值则是对于起点元素，求出其右边的值和下边的值，哪个更小，然后加上自己，就是返回值。
        // dp的优势在于，减少了重复计算。 其实可以从头开始遍历， O(m*n)
        
        
        if(grid == null || grid.length == 0) {
            return -1; //应该是不会出现这种情况。
        }
        
        int m = grid.length;
        int n = grid[0].length;
        
        int [][] memo = new int [m][n];
        memo[m-1][n-1] = grid[m-1][n-1];
        
        for (int i=m-1; i>= 0;i--) {
            for(int j=n-1;j>=0; j--) {
                if (j == n-1 && i == m-1) {
                    continue;
                }
                memo[i][j] = getMin(grid, memo, i, j);
            }
        }
        
        return memo[0][0];
        
    }
    
    private int getMin(int[][] grid,int[][] memo, int i, int j) {
        
        
        int ret = 0;
        if(i<grid.length-1&&j<grid[0].length -1) {
            ret = Math.min(memo[i+1][j],memo[i][j+1]) + grid[i][j];
        } else if (i<grid.length - 1 && j == grid[0].length-1) {   //在最右边一列
            ret = memo[i+1][j] + grid[i][j];
        } else { //在最下面一行
             ret = memo[i][j+1] + grid[i][j];
        }
        
        return ret;
        
        
    }
    
    
    
    
}
