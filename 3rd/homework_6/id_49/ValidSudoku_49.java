class ValidSudoku_49 {
    public boolean isValidSudoku(char[][] board) {
        Set<String> set = new HashSet<String>(120);
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c != '.') {
                    if (!set.add(c + "r" + i)) {
                        return false;
                    }
                    if (!set.add(c + "c" + j)) {
                        return false;
                    }
                    if (!set.add(c + "b" + i / 3 + j / 3)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}