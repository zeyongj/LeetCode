class Solution {
    fun longestString(x: Int, y: Int, z: Int): Int {
        var ans = 0
        if (x == y) {
            ans = 2 * minOf(x, y)
        } else {
            ans = 2 * minOf(x, y) + 1
        }

        ans += z

        return ans * 2
    }
}
