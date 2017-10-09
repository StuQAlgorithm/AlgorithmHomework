package main

func rotate(matrix [][]int) {
	if len(matrix) == 0 {
		return
	}

	n := len(matrix) - 1
	for i := 0; i < n/2+1; i++ {
		for j := 0; j < len(matrix)/2; j++ {
			matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i], matrix[i][j] = matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i]
		}
	}

}
