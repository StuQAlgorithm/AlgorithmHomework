package main

func longestConsecutive(nums []int) int {
	if len(nums) == 0 || len(nums) == 1 {
		return len(nums)
	}

	ret := 1
	mark := make(map[int]struct{}, len(nums))
	visited := make(map[int]struct{}, len(nums))
	for _, v := range nums {
		mark[v] = struct{}{}
	}
	for _, v := range nums {
		if _, ok := visited[v]; ok {
			continue
		}
		visited[v] = struct{}{}
		count, left, right := 0, 0, 0
		vright, vleft := v, v
		for {
			if _, ok := mark[vright+1]; ok {
				visited[vright+1] = struct{}{}
				right++
				vright++
				continue
			}
			break
		}
		for {
			if _, ok := mark[vleft-1]; ok {
				visited[vleft-1] = struct{}{}
				left++
				vleft--
				continue
			}
			break
		}
		count = left + right + 1
		if count > ret {
			ret = count
		}
	}

	return ret
}
