# https://leetcode.com/problems/house-robber-ii/description/
# Note: This is an extension of House Robber.

# After robbing those houses on that street,
# the thief has found himself a new place for
# his thievery so that he will not get too much attention.
# This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.
# since house 0 and n - 1 are now neighbors, we cannot rob them together and thus the solution is now the maximum of

# Rob houses 0 to n - 2;
# Rob houses 1 to n - 1.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        return max(self.rob_in_line(nums, 1, len(nums)), self.rob_in_line(nums, 0, len(nums)-1))

    def rob_in_line(self, nums, l, r):
        """
        :type nums: List[int]
        :rtype: int
        """
        if r - l < 2: return nums[l]
        pre_pre = nums[l]
        pre = max(nums[l], nums[l+1])
        for i in range(l + 2, r):
            pre_pre, pre = pre, max(pre, pre_pre + nums[i])
        return pre

