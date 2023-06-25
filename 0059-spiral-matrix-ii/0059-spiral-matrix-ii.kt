class Solution {
    fun generateMatrix(n: Int): Array<IntArray> {
        val matrix = Array(n) { IntArray(n) }
        var top = 0
        var bottom = n - 1
        var left = 0
        var right = n - 1
        var num = 1

        while (true) {
            for (i in left..right) matrix[top][i] = num++
            if (++top > bottom) break

            for (i in top..bottom) matrix[i][right] = num++
            if (--right < left) break

            for (i in right downTo left) matrix[bottom][i] = num++
            if (--bottom < top) break

            for (i in bottom downTo top) matrix[i][left] = num++
            if (++left > right) break
        }
        return matrix
    }
}
