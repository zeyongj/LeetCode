func twoSum(nums []int, target int) []int {
    m := make(map[int]int, len(nums))
    
    for i, num := range nums {
        if idx, ok := m[target - num]; ok {
            return []int{idx, i}            
        } 
        m[num] = i
    }
    return []int{0, 0}
}