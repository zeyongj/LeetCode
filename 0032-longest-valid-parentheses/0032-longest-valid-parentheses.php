class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function longestValidParentheses($s) {
        $maxLength = 0;
        $stack = [-1]; // Base for calculating the length
        
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] == '(') {
                array_push($stack, $i);
            } else {
                array_pop($stack);
                if (count($stack) == 0) {
                    array_push($stack, $i); // Update the base for length calculation
                } else {
                    $maxLength = max($maxLength, $i - end($stack));
                }
            }
        }
        
        return $maxLength;
    }
}