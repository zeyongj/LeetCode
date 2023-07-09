class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        
        for (i, num) in nums.enumerated() {
            if let index = dict[target-num] {
                if i != index {
                    return [index, i]
                }
            }
            dict[num] = i
        }
        return[0]
    }
}