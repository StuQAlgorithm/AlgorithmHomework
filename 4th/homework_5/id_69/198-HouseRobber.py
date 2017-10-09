# https://leetcode.com/problems/house-robber/description/
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them
# is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
# Also thanks to @ts for adding additional test cases.
# case: [1,0,0,2]
# dp[n] = max( dp[n - 1], dp[n-2] + nums[n] )
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        dp = [None for _ in nums]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums)-1]
# 状态压缩
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums: return 0
#         if len(nums) < 2: return nums[0]
#         pre_pre = nums[0]
#         pre = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             pre_pre, pre = pre, max(pre, pre_pre + nums[i])
#         return pre

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([1,2,3,4,5,6,7,8,9,0]))
