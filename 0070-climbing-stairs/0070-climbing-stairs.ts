class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        if ($n == 1 || $n== 2){
            return $n;
        }
        $step1 = 1;
        $step2 = 1;
        $counter = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $counter = $step1 + $step2;
            $step1 = $step2;
            $step2 = $counter;
        }
        return $counter;
    }
}