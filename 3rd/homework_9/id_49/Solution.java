class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        Queue<int[]> queue = new LinkedList<int[]>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                } else {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        int[][] round = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] ints : round) {
                int row = cell[0] + ints[0];
                int col = cell[1] + ints[1];
                if (row < 0 || row >= m || col < 0 || col >= n || matrix[row][col] <= matrix[cell[0]][cell[1]]) continue;
                matrix[row][col] = matrix[cell[0]][cell[1]] + 1;
                queue.add(new int[]{row, col});
            }
        }
        return matrix;
    }
}