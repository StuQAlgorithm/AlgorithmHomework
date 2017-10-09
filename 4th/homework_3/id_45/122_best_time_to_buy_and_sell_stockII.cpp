//To make max profit
//just need to buy at the lowest point of monotone increasing
//and sell at the highest point of monotone increasing.
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int result = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (prices[i+1] - prices[i] > 0)
                result += prices[i+1] - prices[i];
        }
        return result;
    }
};
