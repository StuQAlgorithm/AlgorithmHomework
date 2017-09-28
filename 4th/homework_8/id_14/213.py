"""
House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a
new place for his thievery so that he will not get too much attention.
This time, all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these houses remain
the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
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
        if count == 2:
            return max(nums[0], nums[1])

        def helper(numbers):
            dp0, dp1, dp2 = 0, numbers[0], 0
            for i in range(1, len(numbers)):
                dp2 = max(dp0 + numbers[i], dp1)
                dp0 = dp1
                dp1 = dp2
            return dp2

        return max(helper(nums[:count - 1]), helper(nums[1:]))

nums = [5, 3, 4, 7]
s = Solution()
money = s.rob(nums)
print(money)

