class Solution {
   fun isPalindrome(x: Int): Boolean {
    if (x < 0)
        return false;
    var number = x
    var reverse = 0
    while (number > 0) {
        reverse = reverse * 10 + number % 10
        number /= 10
    }
    return x == reverse
}
}