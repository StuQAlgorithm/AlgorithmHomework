class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();

        if(matrix == null || matrix.length == 0) return list;

        int rowBegin = 0;
        int colBegin = 0;
        int rowEnd = matrix.length - 1;
        int colEnd = matrix[0].length - 1;

        while(rowBegin <= rowEnd && colBegin <= colEnd){
            //to right
            for(int i = colBegin; i <= colEnd; i++){
                list.add(matrix[rowBegin][i]);
            }
            rowBegin++;

            //to down
            for(int j = rowBegin; j <= rowEnd; j++){
                list.add(matrix[j][colEnd]);
            }
            colEnd--;

            //to left
            if(rowBegin <= rowEnd){
                for(int k = colEnd; k >= colBegin; k--){
                    list.add(matrix[rowEnd][k]);
                }
                rowEnd--;
            }

            //to up
            if(colBegin <= colEnd){
                for(int t = rowEnd; t >= rowBegin; t--){

                    list.add(matrix[t][colBegin]);
                }
                colBegin++;
            }
        }

        return list;
    }
}