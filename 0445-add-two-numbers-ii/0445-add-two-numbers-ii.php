/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {
    public function linkList($array1)
    {
        $array1 = array_values($array1);
        $count = count($array1); 
        $node = null;
        for ($i = $count -1; $i > -1; $i--) {
            $node = new ListNode($array1[$i], $node);
        }     
        
        return $node;
    } 
    
    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */    
    function addTwoNumbers($l1, $l2) {
        $current1 = $l1;
        $num1 = '';
        while ($current1->next) {
            $num1 .= $current1->val;
            $current1 = $current1->next;
        }
        $num1 .= $current1->val;
        
        $current2 = $l2;
        $num2 = '';
        while ($current2->next) {
            $num2 .= $current2->val;
            $current2 = $current2->next;
        }
        $num2 .= $current2->val;
        
        $sum = bcadd($num2, $num1);    
        $sum = str_split($sum);
        
        return $this->linkList($sum);
    }
}