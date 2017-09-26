//Solution 1
class Solution {
public:
    vector<string> result;
    vector<string> generateParenthesis(int n) {
        genParen(n, 0, 0, "");
        return result;
    }
    void genParen(int n, int leftParen, int rightParen, string cur) {
        if (leftParen == n && rightParen == n) {
            result.push_back(cur);
            return;
        }
        if (leftParen < n) {
            genParen(n, leftParen + 1, rightParen, cur + "(");
        }
        if (leftParen > rightParen && rightParen < n) {
            genParen(n, leftParen, rightParen + 1, cur + ")");
        }
    }
};

//Solution 2: dp
/*
 *  the result f(n) will be put an extra () pair to f(n-1). Let the "(" always at the first position, to 
 *  produce a valid result, we can only put ")" in a way that there will be i pairs () inside the extra () 
 *  and n - 1 - i pairs () outside the extra pair.
 *
 *  such as:
 *
 *  f(0): ""
 *
 *  f(1): "("f(0)")"
 *
 *  f(2): "("f(0)")"f(1), "("f(1)")"
 *
 *  f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
 *
 *  So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"*/

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<vector<string> > vvec;
        vector<string> vec;
        vec.push_back("");
        vvec.push_back(vec);
        for (int i = 1; i < n + 1; ++i) {
            vec.clear();
            for (int j = 0; j < i; ++j) {
                for (auto& it1 : vvec[j]) {
                    for (auto& it2 : vvec[i-1-j]) {
                        vec.push_back("(" + it1 + ")" + it2);
                    }   
                }
            }   
            vvec.push_back(vec);
        }
        return vvec[n];
    }
};
