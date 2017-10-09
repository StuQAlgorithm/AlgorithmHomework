package main

import "sort"

func fourSum(nums []int, target int) [][]int {
	if len(nums) < 4 {
		return nil
	}

	sort.Ints(nums)
	results := make([][]int, 0)
	for i := 0; i < len(nums)-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		find3Sum(nums[i+1:], target-nums[i], []int{nums[i]}, &results)
	}

	return results
}

func find3Sum(nums []int, target int, result []int, results *[][]int) {
	if len(nums) < 3 {
		return
	}

	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		ret := append(result, nums[i])
		find2Sum(nums[i+1:], target-nums[i], ret, results)
	}
}

func find2Sum(nums []int, target int, result []int, results *[][]int) {
	if len(nums) < 2 {
		return
	}

	left, right := 0, len(nums)-1
	for left < right {
		if nums[left]+nums[right] == target {
			ret := append(result, nums[left], nums[right])
			*results = append(*results, ret)
			left++
			right--
			for left < right && nums[left] == nums[left-1] {
				left++
			}
			for right > left && nums[right] == nums[right+1] {
				right--
			}
		} else if (nums[left] + nums[right]) < target {
			left++
		} else {
			right--
		}
	}

}
