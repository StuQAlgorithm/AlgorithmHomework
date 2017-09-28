package main

func minimumTotal(triangle [][]int) int {
	length := len(triangle)
	if length == 0 {
		return 0
	}
	if length == 1 {
		return triangle[0][0]
	}

	for k := length - 2; k >= 0; k-- {
		for i := 0; i < len(triangle[k]); i++ {
			left := triangle[k][i] + triangle[k+1][i]
			right := triangle[k][i] + triangle[k+1][i+1]
			if left < right {
				triangle[k][i] = left
			} else {
				triangle[k][i] = right
			}
		}
	}
	return triangle[0][0]
}
