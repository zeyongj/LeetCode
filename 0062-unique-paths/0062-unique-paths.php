class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function uniquePaths($m, $n) {
        $grid = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 || $j == 0) {
                    $grid[$j][$i] = 1;
                } else {
                    $grid[$j][$i] = $grid[$j][$i - 1] + $grid[$j - 1][$i];
                }
            }
        }
        return $grid[$n - 1][$m - 1];
    }
}