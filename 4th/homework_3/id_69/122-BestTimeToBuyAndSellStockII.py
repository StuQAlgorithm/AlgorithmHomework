# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
# 1, 4,3 或则 4，3，2 或则1，2，3
# 每次涨价都卖出
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

