//Solution 1
class Solution {
public:
    int climbStairs(int n) {
        vector<int> result(n + 1, -1);
        result[0] = result[1] = 1;
        climbWays(result, n);
        return result[n];
    }
    int climbWays(vector<int>& result, int level) {
        if (result[level] != -1)
            return result[level];
        return result[level] = climbWays(result, level - 1) + climbWays(result, level - 2);
    }
};

//Solution 2: 
class Solution {
public:
    int climbStairs(int n) {
        vector<int> result(n + 1, -1);
        result[0] = result[1] = 1;
        for (int i = 2; i < n + 1; ++i) {
            result[i] = result[i - 1] + result[i - 2];
        }
        return result[n];
    }
};
