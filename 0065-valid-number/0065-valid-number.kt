class Solution {
    fun isNumber(s: String): Boolean {
        val finals = 0b101101000
        val transfer = arrayOf(
            intArrayOf(0, 1, 6, 2, -1),
            intArrayOf(-1, -1, 6, 2, -1),
            intArrayOf(-1, -1, 3, -1, -1),
            intArrayOf(8, -1, 3, -1, 4),
            intArrayOf(-1, 7, 5, -1, -1),
            intArrayOf(8, -1, 5, -1, -1),
            intArrayOf(8, -1, 6, 3, 4),
            intArrayOf(-1, -1, 5, -1, -1),
            intArrayOf(8, -1, -1, -1, -1)
        )
        var state = 0
        for (c in s) {
            val idx = make(c)
            if (idx < 0) return false
            state = transfer[state][idx]
            if (state < 0) return false
        }
        return (finals and (1 shl state)) > 0
    }

    private fun make(c: Char): Int {
        return when (c) {
            ' ' -> 0
            '+', '-' -> 1
            '.' -> 3
            'e', 'E' -> 4
            in '0'..'9' -> 2
            else -> -1
        }
    }
}
