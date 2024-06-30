object Solution {
    def longestString(x: Int, y: Int, z: Int): Int = {
        var ans = 0
        if (x == y)
            ans = 2 * math.min(x, y)
        else
            ans = 2 * math.min(x, y) + 1

        ans += z

        ans * 2
    }
}
