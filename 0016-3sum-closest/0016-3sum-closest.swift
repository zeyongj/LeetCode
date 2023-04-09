class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        let sortedNums = nums.sorted()
        var closestSum = sortedNums[0] + sortedNums[1] + sortedNums[2]
        var minDiff = abs(target - closestSum)

        for i in 0..<n - 2 {
            var left = i + 1
            var right = n - 1

            while left < right {
                let sum = sortedNums[i] + sortedNums[left] + sortedNums[right]
                let diff = abs(target - sum)

                if diff < minDiff {
                    minDiff = diff
                    closestSum = sum
                }

                if sum < target {
                    left += 1
                } else if sum > target {
                    right -= 1
                } else {
                    return target // The sum is equal to the target, so it's the closest.
                }
            }
        }

        return closestSum
    }
}
