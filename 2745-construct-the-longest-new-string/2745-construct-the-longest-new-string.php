class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $z
     * @return Integer
     */
    function longestString($x, $y, $z) {
        $ans = 0;
        if ($x == $y) {
            $ans = 2 * min($x, $y);
        } else {
            $ans = 2 * min($x, $y) + 1;
        }

        $ans += $z;

        return $ans * 2;
    }
}
