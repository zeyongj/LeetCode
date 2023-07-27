class Solution {

    /**
     * @param String[] $words
     * @param Integer $maxWidth
     * @return String[]
     */
    function fullJustify($words, $maxWidth) {
        $output = [];
        
        $lineWidth = 0;
        $wordsCount = 0;
        $begin = 0;
        $i = 0;
        
        while ($i < count($words)) {
            $word = $words[$i];

            $increase = strlen($word);
            if ($i > $begin) {
                $increase++;
            }
            
			// find one line
            if ($lineWidth + $increase <= $maxWidth) {
                $lineWidth += $increase;
                $i++;
                $wordsCount++;
                continue;
            }
            
			// one line been found, append it to the output
            if ($wordsCount == 1) {
                $output[] = $words[$begin] . str_repeat(' ', $maxWidth - $lineWidth);
            } else {
                $gutter = intdiv($maxWidth - $lineWidth, $wordsCount - 1) + 1;
                $extraGutter = ($maxWidth - $lineWidth) % ($wordsCount - 1);
        
                $aligned = '';

                for ($j = $begin; $j < $i; $j++) {
                    $aligned .= $words[$j];
                    if ($j != $i - 1) {
                        if ($extraGutter > 0) {
                            $aligned .= str_repeat(' ', $gutter + 1);
                            $extraGutter--;
                        } else {
                            $aligned .= str_repeat(' ', $gutter);
                        }
                    }
                }
    
                $output[] = $aligned;
            }

			// find the next line
            $lineWidth = 0;
            $wordsCount = 0;
            $begin = $i;
        }
        
		// append the last line
        $aligned = '';

        for ($j = $begin; $j < $i; $j++) {
            $aligned .= $words[$j];
            if ($j != $i - 1) {
                $aligned .= ' ';
            } else {
                $aligned .= str_repeat(' ', $maxWidth - $lineWidth);
            }
        }
        
        $output[] = $aligned;

        return $output;
    }    
}