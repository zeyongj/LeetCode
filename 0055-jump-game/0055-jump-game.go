func canJump(nums []int) bool {
	reachable := 0
	for i, n := range nums {
		if reachable < i {
			return false
		}
		if i+n > reachable {
			reachable = i + n
		}
	}
	return true  
}