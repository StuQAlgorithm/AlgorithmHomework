package main

func sortColors(nums []int) {
	length := len(nums)
	if length < 2 {
		return
	}
	left, right := 0, length-1
	for i := 0; i < length; i++ {
		for nums[i] == 2 && i < right {
			nums[i], nums[right] = nums[right], nums[i]
			right--
		}
		for nums[i] == 0 && i > left {
			nums[i], nums[left] = nums[left], nums[i]
			left++
		}
	}
}
