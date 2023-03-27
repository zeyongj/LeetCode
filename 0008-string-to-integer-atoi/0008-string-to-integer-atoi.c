#include <stdbool.h>
#include <ctype.h>
#include <limits.h>

int myAtoi(char *s) {
    int i = 0;
    int result = 0;
    int sign = 1;
    
    // Step 1: Read and ignore leading whitespace
    while (s[i] != '\0' && s[i] == ' ') {
        i++;
    }
    
    // Step 2: Check for '-' or '+'
    if (s[i] != '\0' && (s[i] == '-' || s[i] == '+')) {
        if (s[i] == '-') {
            sign = -1;
        }
        i++;
    }
    
    // Step 3: Read digits and convert to integer
    while (s[i] != '\0' && isdigit(s[i])) {
        int digit = s[i] - '0';
        if (result > (INT_MAX / 10) || (result == (INT_MAX / 10) && digit > 7)) {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }
        result = result * 10 + digit;
        i++;
    }
    
    // Apply sign
    result *= sign;
    
    // Step 5: Clamp to the 32-bit signed integer range
    if (result < INT_MIN) {
        return INT_MIN;
    }
    if (result > INT_MAX) {
        return INT_MAX;
    }
    
    // Step 6: Return the final result
    return result;
}
