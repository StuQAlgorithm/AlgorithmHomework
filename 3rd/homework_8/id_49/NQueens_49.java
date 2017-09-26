class NQueens_49 {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ret = new ArrayList<List<String>>();
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        dfs(board, 0, ret);
        return ret;
    }

    private void dfs(char[][] board, int col, List<List<String>> ret) {
        if (col == board.length) {
            List<String> res = new LinkedList<String>();
            for (int i = 0; i < board.length; i++) {
                res.add(new String(board[i]));
            }
            ret.add(res);
            return;
        }
        for (int i = 0; i < board.length; i++) {
            if (validate(board, i, col)) {
                board[i][col] = 'Q';
                dfs(board, col + 1, ret);
                board[i][col] = '.';
            }
        }
    }

    private boolean validate(char[][] board, int row, int col) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'Q' && (row + j == col + i || row + col == i + j || row == i)) {
                    return false;
                }
            }
        }
        return true;
    }
}