class Solution {
    fun longestValidParentheses(s: String): Int {
        var maxLength = 0
        val stack = mutableListOf(-1) // Base for calculating the length

        for (i in s.indices) {
            when (s[i]) {
                '(' -> stack.add(i)
                ')' -> {
                    stack.removeAt(stack.lastIndex)
                    if (stack.isEmpty()) {
                        stack.add(i) // Update the base for length calculation
                    } else {
                        maxLength = maxOf(maxLength, i - stack.last())
                    }
                }
            }
        }

        return maxLength
    }
}