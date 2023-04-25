func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    uniqueIndex := 0
    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[uniqueIndex] {
            uniqueIndex++
            nums[uniqueIndex] = nums[i]
        }
    }

    return uniqueIndex + 1
}