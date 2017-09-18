class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0:
            return None
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target-nums[i]] = i

sol = Solution()
nums = [1, 3, 5, 6]
target = 4
res = sol.twoSum(nums, target)
print(res)