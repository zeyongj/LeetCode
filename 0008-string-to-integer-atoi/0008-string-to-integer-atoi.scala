object Solution {
  def myAtoi(s: String): Int = {
    var i = 0
    var result = 0
    var sign = 1

    // Step 1: Read and ignore leading whitespace
    while (i < s.length && s.charAt(i) == ' ') {
      i += 1
    }

    // Step 2: Check for '-' or '+'
    if (i < s.length && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
      if (s.charAt(i) == '-') {
        sign = -1
      }
      i += 1
    }

    // Step 3: Read digits and convert to integer
    while (i < s.length && s.charAt(i).isDigit) {
      val digit = s.charAt(i) - '0'
      if (result > (Int.MaxValue / 10) || (result == (Int.MaxValue / 10) && digit > 7)) {
        return if (sign == 1) Int.MaxValue else Int.MinValue
      }
      result = result * 10 + digit
      i += 1
    }

    // Apply sign
    result *= sign

    // Step 5: Clamp to the 32-bit signed integer range
    if (result < Int.MinValue) {
      return Int.MinValue
    }
    if (result > Int.MaxValue) {
      return Int.MaxValue
    }

    // Step 6: Return the final result
    result
  }
}
