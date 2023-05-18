class Solution {

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function multiply($num1, $num2) {
        if ($num1 == "0" || $num2 == "0") {
            return "0";
        }
        
        $len1 = strlen($num1);
        $len2 = strlen($num2);
        $result = array_fill(0, $len1 + $len2, 0);
        
        for ($i = $len1 - 1; $i >= 0; $i--) {
            for ($j = $len2 - 1; $j >= 0; $j--) {
                $product = ($num1[$i] - '0') * ($num2[$j] - '0');
                $temp = $product + $result[$i+$j+1];
                $result[$i+$j+1] = $temp % 10;
                $result[$i+$j] += floor($temp / 10);
            }
        }
        
        // Remove leading zeros
        while ($result[0] == 0) {
            array_shift($result);
        }
        
        return implode('', $result);
    }
}