"""
Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count = len(nums)
        if count == 1:
            return nums[0]

        currentMax = minProduct = maxProduct = nums[0]
        for i in range(1, count):
            number = nums[i]
            if number < 0:
                minProduct, maxProduct = maxProduct, minProduct
            maxProduct = max(number, maxProduct * number)
            minProduct = min(number, minProduct * number)
            currentMax = max(maxProduct, currentMax)
        return currentMax

# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#
#         count = len(nums)
#         if count == 1:
#             return nums[0]
#
#         currentMax = minProduct = maxProduct = preMin = preMax= nums[0]
#         for number in nums[1:]:
#             maxProduct = max(number, max(preMin * number, preMax * number))
#             minProduct = min(number, min(preMin * number, preMax * number))
#             currentMax = max(maxProduct, currentMax)
#             preMin, preMax = minProduct, maxProduct
#         return currentMax

nums = [2, 3, -5, 0, 4, 6, -8, 3, -1]
s = Solution()
maxProduct = s.maxProduct(nums)
print(maxProduct)
