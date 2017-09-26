class Solution {
    int[][] dirs = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

    public int[][] updateMatrix(int[][] matrix) {
        if(matrix == null || matrix.length == 0) return null;

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] ret = new int[m][n];
        Queue<int[]> q = new LinkedList<int[]>();

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(matrix[i][j] == 0){
                    q.add(new int[] {i, j});
                }else{
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        while(q.size() > 0){
            int[] cell = q.poll();
            int x, y;
            for(int d = 0; d < dirs.length; d++){
                x = cell[0] + dirs[d][0];
                y = cell[1] + dirs[d][1];

                if(x < 0 || y < 0 || x >= m || y >= n || matrix[cell[0]][cell[1]] >= matrix[x][y]) continue;

                q.add(new int[] {x, y});

                matrix[x][y] = matrix[cell[0]][cell[1]]+1;

            }

        }

        return matrix;

    }

}