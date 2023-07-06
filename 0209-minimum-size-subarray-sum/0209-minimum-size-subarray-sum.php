class Solution
{

    /**
     * @param Integer   $target
     * @param Integer[] $nums
     *
     * @return Integer
     */
    function minSubArrayLen($target, $nums)
    {
        $len = PHP_INT_MAX;

        $count = count($nums);
        for ($i = $j = $s = 0; $i < $count;) {
            $s += $nums[$i++];
            while ($s >= $target) {
                $len = min($len, $i - $j);
                $s -= $nums[$j++];
            }
        }

        return $len < PHP_INT_MAX ? $len : 0;
    }
}