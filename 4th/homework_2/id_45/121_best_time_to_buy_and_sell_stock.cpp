class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int cur_min_in = INT_MAX;
        int cur_profit = 0;
        for (int i = 0; i < n; ++i) {
            cur_profit = max(cur_profit, prices[i] - cur_min_in);
            cur_min_in = min(cur_min_in, prices[i]);
        }
        return cur_profit;
    }
};
