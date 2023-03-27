public class Solution {
    public int myAtoi(String s) {
        int i = 0;
        int result = 0;
        int sign = 1;
        
        // Step 1: Read and ignore leading whitespace
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }
        
        // Step 2: Check for '-' or '+'
        if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            if (s.charAt(i) == '-') {
                sign = -1;
            }
            i++;
        }
        
        // Step 3: Read digits and convert to integer
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            if (result > (Integer.MAX_VALUE / 10) || (result == (Integer.MAX_VALUE / 10) && digit > 7)) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            result = result * 10 + digit;
            i++;
        }
        
        // Apply sign
        result *= sign;
        
        // Step 5: Clamp to the 32-bit signed integer range
        if (result < Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }
        if (result > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        }
        
        // Step 6: Return the final result
        return result;
    }
}
