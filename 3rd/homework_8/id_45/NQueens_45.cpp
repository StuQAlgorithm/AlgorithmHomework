class Solution {
public:
    vector<vector<int>> vvec;
    set<int> col, slash, backlash;
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        if (n < 1)
            return result;
        deque<int> cur;
        findNQueens(vvec, 0, n, cur);
        int cnt = vvec.size();
        vector<int> vec;
        for (int i = 0; i < cnt; ++i) {
            vector<string> vstr;
            vec = vvec[i];
            for (int j = 0; j < n; ++j) {
                string s(n, '.');
                s[vec[j]] = 'Q';
                vstr.push_back(s);
            }   
            result.push_back(vstr);
        }   
        return result;
    }
    void findNQueens(vector<vector<int>>& vvec, int level, int n, deque<int>& cur) {
        if (level == n) {
            vector<int> vec(cur.begin(), cur.end());
            vvec.push_back(vec);
            return;
        }   
        for (int i = 0; i < n; ++i) {
            if (col.find(i) == col.end() &&
                    slash.find(level + i) == slash.end() &&
                    backlash.find(level - i) == backlash.end()) {
                col.insert(i);
                slash.insert(level+i);
                backlash.insert(level-i);
                cur.push_back(i);
                findNQueens(vvec, level + 1, n, cur);
                cur.pop_back();
                backlash.erase(level-i);
                slash.erase(level+i);
                col.erase(i);
            }
        }
        return;
    }
};
