import (
	"fmt"
	"math"
	"strings"
	"unicode"
)

func myAtoi(s string) int {
	i := 0
	result := 0
	sign := 1

	// Step 1: Read and ignore leading whitespace
	for i < len(s) && s[i] == ' ' {
		i++
	}

	// Step 2: Check for '-' or '+'
	if i < len(s) && (s[i] == '-' || s[i] == '+') {
		if s[i] == '-' {
			sign = -1
		}
		i++
	}

	// Step 3: Read digits and convert to integer
	for i < len(s) && unicode.IsDigit(rune(s[i])) {
		digit := int(s[i] - '0')
		if result > math.MaxInt32/10 || (result == math.MaxInt32/10 && digit > 7) {
			if sign == 1 {
				return math.MaxInt32
			} else {
				return math.MinInt32
			}
		}
		result = result*10 + digit
		i++
	}

	// Apply sign
	result *= sign

	// Step 5: Clamp to the 32-bit signed integer range
	if result < math.MinInt32 {
		return math.MinInt32
	}
	if result > math.MaxInt32 {
		return math.MaxInt32
	}

	// Step 6: Return the final result
	return result
}
