# https://leetcode.com/problems/sliding-window-median/description/
import bisect


class Solution(object):

    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        res = [(window[k / 2] + window[(k - 1) / 2]) / 2.0]

        for i in range(k, len(nums)):
            del window[bisect.bisect_left(window, nums[i - k])]
            bisect.insort(window, nums[i])
            res.append((window[k / 2] + window[(k - 1) / 2]) / 2.0)
        return res
