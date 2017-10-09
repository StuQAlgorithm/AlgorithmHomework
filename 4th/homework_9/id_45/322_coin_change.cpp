class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int upperBound = amount + 1;
        vector<int> result(amount + 1, upperBound);
        result[0] = 0;
        for (int i = 0; i < coins.size(); ++i) {
            for (int money = coins[i]; money < amount + 1; ++money) {
                result[money] = min(result[money], result[money - coins[i]] + 1);
            }
        }
        return result[amount] < upperBound? result[amount] : -1;
    }
};
