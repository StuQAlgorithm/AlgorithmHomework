class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        pre1 = 0
        result1 = 0
        for i in range(1, n):
            temp = pre1
            pre1 = result1
            result1 = max(temp + nums[i], pre1)

        pre2 = 0
        result2 = 0
        for i in range(0, n - 1):
            temp = pre2
            pre2 = result2
            result2 = max(temp + nums[i], pre2)

        return max(result1, result2)
    