func insert(intervals [][]int, newInterval []int) [][]int {
    if len(intervals) == 0 {
        return append([][]int{}, newInterval)
    }
    
    if intervals[0][1] < newInterval[0] {
        return append(append([][]int{},intervals[0]),
                      insert(intervals[1:], newInterval)...)
    }
    
    if intervals[0][1] >= newInterval[0] && intervals[0][1] <= newInterval[1] {
        return append([][]int{},
                      insert(intervals[1:],
                             []int{min(intervals[0][0], newInterval[0]),
                                   newInterval[1]})...)
    }
    
    if intervals[0][1] >= newInterval[1] && intervals[0][0] <= newInterval[1] {
        intervals[0][0] = min(intervals[0][0], newInterval[0])
        return intervals
    }
    
    if intervals[0][0] > newInterval[1] {
        return append(append([][]int{}, newInterval), intervals...)
    }
    
    return nil
    
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}