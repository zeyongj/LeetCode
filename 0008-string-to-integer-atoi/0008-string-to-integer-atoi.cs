using System;

public class Solution {
    public int MyAtoi(string s) {
        int i = 0;
        int result = 0;
        int sign = 1;
        
        // Step 1: Read and ignore leading whitespace
        while (i < s.Length && s[i] == ' ') {
            i++;
        }
        
        // Step 2: Check for '-' or '+'
        if (i < s.Length && (s[i] == '-' || s[i] == '+')) {
            if (s[i] == '-') {
                sign = -1;
            }
            i++;
        }
        
        // Step 3: Read digits and convert to integer
        while (i < s.Length && Char.IsDigit(s[i])) {
            int digit = s[i] - '0';
            if (result > (Int32.MaxValue / 10) || (result == (Int32.MaxValue / 10) && digit > 7)) {
                return (sign == 1) ? Int32.MaxValue : Int32.MinValue;
            }
            result = result * 10 + digit;
            i++;
        }
        
        // Apply sign
        result *= sign;
        
        // Step 5: Clamp to the 32-bit signed integer range
        if (result < Int32.MinValue) {
            return Int32.MinValue;
        }
        if (result > Int32.MaxValue) {
            return Int32.MaxValue;
        }
        
        // Step 6: Return the final result
        return result;
    }
}
