class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isNumber($s) {
        $state = array_fill(0, 10, 0);
        $finals = 0b101101000;
        $transfer = [
            [ 0, 1, 6, 2, -1],
            [-1,-1, 6, 2, -1],
            [-1,-1, 3, -1, -1],
            [ 8,-1, 3, -1, 4],
            [-1, 7, 5, -1, -1],
            [ 8,-1, 5, -1, -1],
            [ 8,-1, 6, 3, 4],
            [-1,-1, 5, -1, -1],
            [ 8,-1,-1, -1, -1]
        ];
        $idx = 0;
        $chars = str_split($s);
        foreach ($chars as $c) {
            $idx = $this->make($c);
            if ($idx < 0) return false;
            $state[0] = $transfer[$state[0]][$idx];
            if ($state[0] < 0) return false;
        }
        return ($finals & (1 << $state[0])) > 0;
    }

    private function make($c) {
        switch ($c) {
            case ' ': return 0;
            case '+': 
            case '-': return 1;
            case '.': return 3;
            case 'e': 
            case 'E': return 4;
            default:
                if (ctype_digit($c)) return 2;
                return -1;
        }
    }
}
