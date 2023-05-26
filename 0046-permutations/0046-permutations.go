func permute(nums []int) [][]int {
    var result [][]int
    permuteHelper(nums, 0, &result)
    return result
}

func permuteHelper(nums []int, start int, result *[][]int) {
    if start == len(nums) {
        permutation := make([]int, len(nums))
        copy(permutation, nums)
        *result = append(*result, permutation)
        return
    }

    for i := start; i < len(nums); i++ {
        nums[start], nums[i] = nums[i], nums[start] // swap
        permuteHelper(nums, start+1, result)
        nums[start], nums[i] = nums[i], nums[start] // backtrack
    }
}
