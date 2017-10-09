package main

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}
	if n == 1 {
		return 10
	}
	if n > 10 {
		return 0
	}

	ret := 10
	count := 9
	step := 9
	for i := 2; i <= n; i++ {
		step *= count
		ret += step
		if i == n {
			break
		}
		count--
	}
	return ret
}
