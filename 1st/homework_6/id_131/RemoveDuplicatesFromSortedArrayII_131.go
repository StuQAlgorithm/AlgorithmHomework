package main

func removeDuplicates(nums []int) int {
	length := len(nums)
	if length <= 2 {
		return length
	}

	i := 2
	for j, k := 0, 2; k < length; k++ {
		if nums[k] > nums[j] {
			nums[i] = nums[k]
			i++
			j++
		}
	}
	nums = nums[:i]

	return i
}
