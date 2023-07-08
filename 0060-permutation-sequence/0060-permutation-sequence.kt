class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getPermutation($n, $k) {
        if ($n == 0) return '';
        
        $numbers = range(1, $n);
        $isVisited = array_fill(0, $n, false);
        $result = [];
        $numberGenerated = 0;
        
        $this->generateSequence($result, [], $isVisited, $numbers, $numberGenerated, $k);
        
        return implode('', $result);
    }

    function generateSequence(&$array, $currentSequence, &$isVisited, $numbers, &$numberGenerated, $k) {
        if ($k <= $numberGenerated) {
            return;
        }
        
        if (count($currentSequence) == count($numbers)) {
            $array = $currentSequence;
            $numberGenerated++;
            return;
        }
        
        $remaining = count($numbers) - count($currentSequence);
        $factorial = $this->factorial($remaining - 1);
        
        for ($i = 0; $i < count($numbers); $i++) {
            if (!$isVisited[$i]) {
                if ($k > $numberGenerated + $factorial) {
                    $numberGenerated += $factorial;
                    continue;
                }
                
                $isVisited[$i] = true;
                $currentSequence[] = $numbers[$i];
                $this->generateSequence($array, $currentSequence, $isVisited, $numbers, $numberGenerated, $k);
                $isVisited[$i] = false;
                array_pop($currentSequence);
            }
        }
    }
    
    function factorial($n) {
        if ($n <= 1) return 1;
        return $n * $this->factorial($n - 1);
    }
}