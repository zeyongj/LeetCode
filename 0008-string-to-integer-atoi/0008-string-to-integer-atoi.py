class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        result = 0
        sign = 1
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Read and ignore leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check for '-' or '+'
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Read digits and convert to integer
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (INT_MAX // 10) or (result == (INT_MAX // 10) and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        # Apply sign
        result *= sign
        
        # Step 5: Clamp to the 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        # Step 6: Return the final result
        return result
