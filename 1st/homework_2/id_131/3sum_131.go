package main

import "sort"

func threeSum(nums []int) [][]int {
	ret := make([][]int, 0)
	length := len(nums)
	if length == 0 {
		return ret
	}
	sort.Ints(nums)

	for i := 0; i < length-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		k := length - 1
		target := -nums[i]
		for j := i + 1; j < k; {
			if (nums[j] + nums[k]) == target {
				ret = append(ret, []int{nums[i], nums[j], nums[k]})
				j++
				k--
				for j < k && nums[j] == nums[j-1] {
					j++
				}
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else if (nums[j] + nums[k]) > target {
				k--
			} else {
				j++
			}

		}
	}
	return ret
}
