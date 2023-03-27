class Solution {
    fun myAtoi(s: String): Int {
        var i = 0
        var result = 0
        var sign = 1

        // Step 1: Read and ignore leading whitespace
        while (i < s.length && s[i] == ' ') {
            i++
        }

        // Step 2: Check for '-' or '+'
        if (i < s.length && (s[i] == '-' || s[i] == '+')) {
            if (s[i] == '-') {
                sign = -1
            }
            i++
        }

        // Step 3: Read digits and convert to integer
        while (i < s.length && s[i].isDigit()) {
            val digit = s[i].toInt() - '0'.toInt()
            if (result > Int.MAX_VALUE / 10 || (result == Int.MAX_VALUE / 10 && digit > 7)) {
                return if (sign == 1) Int.MAX_VALUE else Int.MIN_VALUE
            }
            result = result * 10 + digit
            i++
        }

        // Apply sign
        result *= sign

        // Step 5: Clamp to the 32-bit signed integer range
        if (result < Int.MIN_VALUE) {
            return Int.MIN_VALUE
        }
        if (result > Int.MAX_VALUE) {
            return Int.MAX_VALUE
        }

        // Step 6: Return the final result
        return result
    }
}
