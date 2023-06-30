class Solution {

    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer
     */
    function uniquePathsWithObstacles($obstacleGrid) {
        $row = count($obstacleGrid);
        $column = count($obstacleGrid[0]);
        for ($i = 0; $i < $row; $i++) {
            for ($j = 0; $j < $column; $j++) {
                if ($obstacleGrid[$i][$j] == 1) {
                    $obstacleGrid[$i][$j] = 0;
                } else if ($i == 0 && $j == 0) {
                    $obstacleGrid[$i][$j] = 1;
                } else {
                    $obstacleGrid[$i][$j] = $obstacleGrid[$i - 1][$j] + $obstacleGrid[$i][$j - 1];
                }
            }
        }
        return $obstacleGrid[$row - 1][$column - 1];
    }
}