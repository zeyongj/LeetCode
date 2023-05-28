import (
    "sort"
)

func permuteUnique(nums []int) [][]int {
    sort.Ints(nums)
    result := [][]int{}
    backtrack(&result, []int{}, nums, make([]bool, len(nums)))
    return result
}

func backtrack(result *[][]int, temp []int, nums []int, used []bool) {
    if len(temp) == len(nums) {
        tempCopy := make([]int, len(temp))
        copy(tempCopy, temp)
        *result = append(*result, tempCopy)
        return
    }
    for i := 0; i < len(nums); i++ {
        if used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1]) {
            continue
        }
        used[i] = true
        temp = append(temp, nums[i])
        backtrack(result, temp, nums, used)
        used[i] = false
        temp = temp[:len(temp)-1]
    }
}
