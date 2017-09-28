class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]
            i = i + 1

        return profit
