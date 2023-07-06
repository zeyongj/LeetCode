class Solution {
    func minSubArrayLen(_ t: Int, _ n: [Int]) -> Int {
        var size = Int.max, start = 0, sum = 0
        for (a,b) in n.enumerated() {
            sum += b
            while sum >= t, start <= a {
                size = min(size, a - start + 1)
                sum -= n[start]
                start += 1
            }
        }
        return size == .max ? 0 : size
    }
}