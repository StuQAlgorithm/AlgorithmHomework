class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        curSum, maxSum = nums[0], nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum+num)
            maxSum = max(maxSum, curSum)
        return maxSum