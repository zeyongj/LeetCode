class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function isMatch($s, $p) {
        $m = strlen($s);
        $n = strlen($p);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, false));

        // base cases
        $dp[0][0] = true;
        for ($j = 1; $j <= $n; ++$j) {
            if ($p[$j - 1] != '*') break;
            $dp[0][$j] = true;
        }

        // dynamic programming
        for ($i = 1; $i <= $m; ++$i) {
            for ($j = 1; $j <= $n; ++$j) {
                if ($p[$j - 1] == '*') {
                    $dp[$i][$j] = $dp[$i - 1][$j] || $dp[$i][$j - 1];
                } else if ($p[$j - 1] == '?' || $s[$i - 1] == $p[$j - 1]) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1];
                }
            }
        }

        return $dp[$m][$n];
    }
}
