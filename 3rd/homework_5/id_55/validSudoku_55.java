class Solution {
    //看似每个格都要检查行、列、内盒， 但其实相同行(列，内盒)对某个数字，就只能出现一次，因此用一个hashSet再加上坐标信息就都容进去了
    //O(N*N*N*N*N) -> O(N*N)
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> hash = new HashSet<String>();
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                char cell = board[i][j];
                if(cell != '.'){
                    if(!hash.add(cell + " in row " + i)
                            || !hash.add(cell + " in col " + j)
                            || !hash.add(cell + " in box " + i/3 + j/3)
                            ) return false;
                }
            }
        }

        return true;
    }
}