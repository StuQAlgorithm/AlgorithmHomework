# UNDONE
# Status: Time Limit Exceeded


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not amount:
            return 0

        count = amount + 1
        for i in range(len(coins)):
            curr_val = 0
            if amount >= coins[i]:
                next_val = self.coinChange(coins, amount - coins[i])
                if next_val > -1:
                    curr_val = 1 + next_val
            if curr_val > 0:
                count = min(count, curr_val)

        if count == amount + 1:
            count = -1
        return count
