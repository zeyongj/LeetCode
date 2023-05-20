class Solution {

    private $graph = [];

    /**
     * @param String[][] $equations
     * @param Float[] $values
     * @param String[][] $queries
     * @return Float[]
     */
    function calcEquation($equations, $values, $queries) {
        for ($i = 0; $i < count($equations); $i++) {
            $equation = $equations[$i];
            if (!isset($this->graph[$equation[0]])) {
                $this->graph[$equation[0]] = [];
            }
            if (!isset($this->graph[$equation[1]])) {
                $this->graph[$equation[1]] = [];
            }
            $this->graph[$equation[0]][$equation[1]] = $values[$i];
            $this->graph[$equation[1]][$equation[0]] = 1 / $values[$i];
        }

        $result = [];
        for ($i = 0; $i < count($queries); $i++) {
            $query = $queries[$i];
            array_push($result, $this->DFS($query[0], $query[1], []));
        }
        return $result;
    }

    private function DFS($start, $end, $visited) {
        if (!isset($this->graph[$start])) return -1.0;
        if (isset($this->graph[$start][$end])) return $this->graph[$start][$end];

        $visited[$start] = true;
        foreach ($this->graph[$start] as $neighbor => $value) {
            if (isset($visited[$neighbor])) continue;
            $product = $this->DFS($neighbor, $end, $visited);
            if ($product != -1.0) return $value * $product;
        }
        return -1.0;
    }
}
