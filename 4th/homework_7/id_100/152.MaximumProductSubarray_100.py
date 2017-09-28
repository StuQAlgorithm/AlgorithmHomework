class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        result = nums[0]
        minNum, maxNum = result, result
        for i in range(1, len(nums)):
            temp = maxNum
            maxNum = max(max(nums[i] * temp, nums[i] * minNum), nums[i])
            minNum = min(min(nums[i] * temp, nums[i] * minNum), nums[i])
            result = max(maxNum, result)
            
        return result
    