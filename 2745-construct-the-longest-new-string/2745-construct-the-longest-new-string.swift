class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        var ans = 0
        if x == y {
            ans = 2 * min(x, y)
        } else {
            ans = 2 * min(x, y) + 1
        }

        ans += z

        return ans * 2
    }
}
