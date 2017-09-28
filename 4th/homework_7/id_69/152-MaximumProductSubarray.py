# https://leetcode.com/problems/maximum-product-subarray/description/
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# dp_min[n] min_production until n
# dp_max[n] max_production until n
#
# dp_max[n] = max(dp_max[n-1]*nums[n], dp_min[n-1]*nums[n]) or nums[n]
# dp_min[n] = min(dp_max[n-1]*nums[n], dp_min[n-1]*nums[n]) or nums[n]

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        pre_max, pre_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(pre_max*nums[i], pre_min*nums[i], nums[i])
            cur_min = min(pre_max*nums[i], pre_min*nums[i], nums[i])
            res = max(cur_max, res)
            pre_max, pre_min = cur_max, cur_min
        return res

if __name__ == '__main__':
  sol = Solution()
  print(sol.maxProduct([2, 3, -2, 4, -2, -1, 100]))
