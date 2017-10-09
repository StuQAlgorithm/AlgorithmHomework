"""
Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            val = prices[i] - prices[i - 1]
            if val > 0:
                profit += val
        return profit


prices = [7, 1, 5, 3, 6, 4, 8]
s = Solution()
profit = s.maxProfit(prices)
print(profit)
