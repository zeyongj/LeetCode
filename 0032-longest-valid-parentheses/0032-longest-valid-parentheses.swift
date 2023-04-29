class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var maxLength = 0
        var stack = [-1] // Base for calculating the length
        
        for (i, char) in s.enumerated() {
            if char == "(" {
                stack.append(i)
            } else {
                stack.removeLast()
                if stack.isEmpty {
                    stack.append(i) // Update the base for length calculation
                } else {
                    maxLength = max(maxLength, i - stack.last!)
                }
            }
        }
        return maxLength
    }
}