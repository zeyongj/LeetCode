class Solution {

    /**
     * @param Integer $n
     * @return Integer[][]
     */
    function generateMatrix($n) {
        $matrix=array();
        for ($i=0; $i <$n ; $i++) { 
            for ($j=0; $j < $n; $j++) { 
                $matrix[$i][$j]=0;
            }
        }
        $i=1;
        $top=0;
        $bottom=$n-1;
        $left=0;
        $ritht=$n-1;
        $direction=0;
        while ($i<=$n*$n) 
        {
            if ($direction==0) 
            {
                for ($j=$left; $j <=$ritht ; $j++) 
                { 
                    $matrix[$top][$j]=$i++;
                    
                }
                $top++;
            }
            elseif ($direction==1) 
            {
                for ($j=$top; $j <=$bottom ; $j++) 
                { 
                    $matrix[$j][$ritht]=$i++;
                }
                $ritht--;
            }
            elseif ($direction==2) {
            for ($j=$ritht; $j >=$left ; $j--) { 
                $matrix[$bottom][$j]=$i++;
            }
            $bottom--;
            }
            else {
            for ($j=$bottom; $j >=$top ; $j--) { 
                $matrix[$j][$left]=$i++;
            }
            $left++;
            }
            $direction=($direction+1)%4;
        
        }
        return $matrix;
    }
}