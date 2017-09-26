class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ret = new ArrayList<>();
        if(n == 0) return ret;

        char[][] grid = new char[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                grid[i][j] = '.';
            }
        }

        dfs(ret, 0, grid);

        return ret;
    }

    public void dfs(List<List<String>> ret, int col, char[][] grid){
        if(col == grid.length){
            ret.add(buildCopyOut(grid));
            return;
        }

        for(int i = 0; i < grid.length; i++){
            if( isValid(grid, i, col) ){
                grid[i][col] = 'Q';
                dfs(ret, col+1, grid);
                grid[i][col] = '.'; //reset
            }
        }
    }

    public boolean isValid(char[][] grid, int m, int n){
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 'Q'
                        && (   (i-m == j-n) //135°
                        || (i-m == n-j) //45°
                        || (i == m) )   //same row and same col
                        )
                    return false;
            }
        }

        return true;
    }

    public List<String> buildCopyOut(char[][] grid){
        List<String> list = new ArrayList<String>();
        for(int i = 0; i < grid.length; i++){
            String s = new String(grid[i]);
            list.add(s);
        }

        return list;
    }
}