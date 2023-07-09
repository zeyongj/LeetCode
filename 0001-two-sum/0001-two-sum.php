class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $res = [];
        $setSum = [];
        
        for($i = 0; $i < sizeof($nums); $i++)
        {
            $diff = $target - $nums[$i];
            if(array_search($diff, $setSum) !== false)
            {
                $key = array_search($diff, $setSum);
                $res[] = $i;
                $res[] = $key;
            }
            $setSum[] = $nums[$i];
        }
        return $res;
    }
}