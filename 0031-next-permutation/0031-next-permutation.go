
import "fmt"

func swap(nums []int, i, j int) {
    nums[i], nums[j] = nums[j], nums[i]
}

func reverse(nums []int, start, end int) {
    for start < end {
        swap(nums, start, end)
        start++
        end--
    }
}

func nextPermutation(nums []int) {
    i := len(nums) - 2
    for i >= 0 && nums[i] >= nums[i+1] {
        i--
    }
    if i >= 0 {
        j := len(nums) - 1
        for j > i && nums[j] <= nums[i] {
            j--
        }
        swap(nums, i, j)
    }
    reverse(nums, i+1, len(nums)-1)
}