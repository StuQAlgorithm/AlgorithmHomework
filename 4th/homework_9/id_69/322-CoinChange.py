# https://leetcode.com/problems/coin-change/description/

# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
import sys
from collections import deque
class Solution(object):
    # dp
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins: return -1
        if amount == 0: return 0
        MAX = 0x7fffffff # Using float("inf") would be slower.
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
        return dp[amount] if dp[amount] < MAX  else -1
        # [dp[amount], -1][dp[amount] == MAX]

    # bst
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins: return -1
        if amount == 0: return 0
        value = deque([0])
        size = len(value)
        count =  0
        visited = set(value)
        while value:
            count += 1
            for i in range(size):
                v = value.popleft()
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return count
                    elif newval > amount:
                        continue
                    elif newval not in visited:
                        visited.add(newval)
                        value.append(newval)
            size = len(value)
        return -1



if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange([1],1)) # [1], 0 ; [1],1 ; [1,2,5], 100



