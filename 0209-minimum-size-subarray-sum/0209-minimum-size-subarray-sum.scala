func minSubArrayLen(target int, nums []int) int {
    	left, currSum := 0, 0

	minLen := float64(len(nums) + 1)

	for right := 0; right < len(nums); right++ {
		currSum += nums[right]
		for currSum >= target {
			minLen = math.Min(minLen, float64(right-left+1))
			currSum -= nums[left]
			left++
		}

	}
	if minLen == float64(len(nums)+1) {
		return 0
	}

	return int(minLen)
}