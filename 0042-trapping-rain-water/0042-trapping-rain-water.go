func trap(height []int) int {
    left := 0
    right := len(height) - 1
    left_max := 0
    right_max := 0
    total_water := 0

    for left < right {
        if height[left] < height[right] {
            if height[left] > left_max {
                left_max = height[left]
            } else {
                total_water += left_max - height[left]
            }
            left++;
        } else {
            if height[right] > right_max {
                right_max = height[right]
            } else {
                total_water += right_max - height[right]
            }
            right--
        }
    }
    return total_water
}