"""
House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
 determine the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):

    # 8, 3, 4, 5
    # |               n = 0, f0 = a[0]                  8
    # |--|            n = 1 f1 = max(0 + a[1], f0)      8
    # |--|--|         n = 2 f2 = max(f0 + a[2], f1)     12
    # |--|--|--|      n = 3 f3 = max(f1 + a[3], f2)     13

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = len(nums)
        if count == 1:
            return nums[0]

        dp0, dp1, dp2 = 0, nums[0], 0
        for i in range(1, len(nums)):
            dp2 = max(dp0 + nums[i], dp1)
            dp0 = dp1
            dp1 = dp2

        return dp2

nums = [8, 3, 4, 5, 2]
s = Solution()
money = s.rob(nums)
print(money)




