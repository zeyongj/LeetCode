func climbStairs(n int) int {

	if n <= 3 {
		return n
	}

	ans := 0
	end := n - 3
	prev2 := 2
	prev1 := 3

	for i := 0; i < end; i++ {
		ans = prev2 + prev1
		prev2, prev1 = prev1, ans
	}

	return ans

}