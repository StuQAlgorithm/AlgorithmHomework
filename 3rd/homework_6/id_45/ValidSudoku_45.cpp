//36.Valid Soduku
class Solution {
public:
    vector<set<char> > col, row;
    vector<vector<set<char> > > sub;
    bool isValidSudoku(vector<vector<char> >& board) {
        if (board.size() == 0 || board[0].size() == 0)
            return false;
        int n = board.size();
        int m = board[0].size();
        int r_index, c_index, filledBlank = 0;
        //preprocess;
        for (int i = 0; i < n / 3; ++i) {
            vector<set<char> > sub_row;
            for (int j = 0; j < m / 3; ++j) {
                r_index = i * 3;
                c_index = j * 3;
                set<char> se;
                for (int k = r_index; k < r_index + 3; ++k) {
                    for (int l = c_index; l < c_index + 3; ++l) {
                        if (row.size() < k + 1) {
                            set<char> row_set;
                            row.push_back(row_set);
                        }
                        if (col.size() < l + 1) {
                            set<char> col_set;
                            col.push_back(col_set);
                        }
                        if (board[k][l] != '.') {
                            ++filledBlank;
                            //check whether the initial board is valid;
                            if (row[k].find(board[k][l]) != row[k].end() ||
                                    col[l].find(board[k][l]) != col[l].end() ||
                                    se.find(board[k][l]) != se.end()) {
                                return false;
                            }

                            row[k].insert(board[k][l]);
                            col[l].insert(board[k][l]);
                            se.insert(board[k][l]);
                        }
                    }
                }
                sub_row.push_back(se);
            }
            sub.push_back(sub_row);
        }
        return true;
    }
};

//37.Soduku Solver
class Solution {
public:
    vector<set<char> > col, row;
    vector<vector<set<char> > > sub;
    void solveSudoku(vector<vector<char> >& board) {
        bool result = false;
        if (board.size() == 0 || board[0].size() == 0)
            return;
        int n = board.size();
        int m = board[0].size();
        int r_index, c_index, filledBlank = 0;
        //preprocess;
        for (int i = 0; i < n / 3; ++i) {
            vector<set<char> > sub_row;
            for (int j = 0; j < m / 3; ++j) {
                r_index = i * 3;
                c_index = j * 3;
                set<char> se;
                for (int k = r_index; k < r_index + 3; ++k) {
                    for (int l = c_index; l < c_index + 3; ++l) {
                        if (row.size() < k + 1) {
                            set<char> row_set;
                            row.push_back(row_set);
                        }
                        if (col.size() < l + 1) {
                            set<char> col_set;
                            col.push_back(col_set);
                        }
                        if (board[k][l] != '.') {
                            ++filledBlank;
                            row[k].insert(board[k][l]);
                            col[l].insert(board[k][l]);
                            se.insert(board[k][l]);
                        }
                    }
                }
                sub_row.push_back(se);
            }
            sub.push_back(sub_row);
        }

        int remainBlank = n * m - filledBlank;
        judgeSudoku(board, n, m, remainBlank);
    }
    bool judgeSudoku(vector<vector<char> >& board, int n, int m, int remainBlank) {
        if (remainBlank == 0) {
            return true;
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; ++c) {
                        if ((row[i].size() == 0 || row[i].find(c) == row[i].end()) &&
                                (col[j].size() == 0 || col[j].find(c) == col[j].end()) &&
                                (sub[i/3][j/3].size() == 0 || sub[i/3][j/3].find(c) == sub[i/3][j/3].end())) {
                            board[i][j] = c;
                            row[i].insert(c);
                            col[j].insert(c);
                            sub[i/3][j/3].insert(c);

                            if (judgeSudoku(board, n, m, remainBlank - 1))
                                return true;

                            row[i].erase(c);
                            col[j].erase(c);
                            sub[i/3][j/3].erase(c);
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return false;
    }
};
