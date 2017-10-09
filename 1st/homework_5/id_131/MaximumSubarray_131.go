package main

import "math"

func maxSubArray(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	sum, max := 0, int(math.MinInt64)
	for _, v := range nums {
		if sum > 0 {
			sum += v
		} else {
			sum = v
		}
		if sum > max {
			max = sum
		}
	}
	return max
}
