class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        top = 0
        times = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[top]:
                times += 1
                if times <= 2:
                    top += 1
                    nums[top] = nums[i]
                else:
                    times += 1
            else:
                times = 1
                top += 1
                nums[top] = nums[i]
        return top+1
