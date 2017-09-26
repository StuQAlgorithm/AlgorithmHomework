class Solution {
    public void rotate(int[][] matrix) {
        if(matrix == null || matrix.length == 0) return;

        int n = matrix.length;

        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                swap(matrix, i, j, j, i);

            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n/2; j++){
                swap(matrix, i, j, i, n - j -1);
            }
        }
    }

    public void swap(int[][] matrix, int p1, int p2, int q1, int q2){
        int t = matrix[p1][p2];
        matrix[p1][p2] = matrix[q1][q2];
        matrix[q1][q2] = t;
    }
}