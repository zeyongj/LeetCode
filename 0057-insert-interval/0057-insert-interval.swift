// Time complexity: O(n)
// Space complexity: O(n)
class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        var result = [[Int]]()
        var newInterval = newInterval

        // Conditions:
        // - if the new interval end value is before the current interval start value 
        // - if the start value of the new interval is greater than the end value of the interval we are in
        // - if both are untrue then we have an overlap
        for i in 0..<intervals.count {
            if newInterval[1] < intervals[i][0] {
                result.append(newInterval)  
                //return here because we know all of the intervals that come after are not overlapping
                return result + intervals[i...(intervals.count - 1)]
            } else if newInterval[0] > intervals[i][1] {
                result.append(intervals[i])
            } else {
                let val1 = min(intervals[i][0], newInterval[0])
                let val2 = max(intervals[i][1], newInterval[1])
                newInterval = [val1, val2]
            }
        }
        
        // if we get here, that means that we didn't execute the first if statement and the append newInterval was never called - let's add it here
        result.append(newInterval)
        
        return result  
    }
}