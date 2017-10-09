class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        profit = 0
        min = prices[0]
        l = len(prices)
        for i in range(l):
            if prices[i] < min:
                min = prices[i]
            else:
                if profit < prices[i] - min:
                    profit = prices[i] - min;

        return profit
