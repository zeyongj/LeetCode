func longestValidParentheses(s string) int {
    maxLength := 0
    stack := []int{-1} // Base for calculating the length

    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            stack = append(stack, i)
        } else {
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                stack = append(stack, i) // Update the base for length calculation
            } else {
                maxLength = max(maxLength, i-stack[len(stack)-1])
            }
        }
    }
    return maxLength
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
