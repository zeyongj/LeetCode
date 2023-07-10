/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function minDepth($root) {
        // return 0 depth if node is null
       if ($root === null) return 0;
        // calculate the left node depth
        $li_leftDepth = $this->minDepth($root->left);
        // calculate the right node depth
        $li_rightDepth = $this->minDepth($root->right);
        // now compare
        // return 1+left node depth (left node total depth)
        // if left node depth less then right node depth and left has at least 1 depth
        // or right node depth is less than 1
        // otherwise it returns the right node depth+1

        return ($li_leftDepth<$li_rightDepth && $li_leftDepth>0 || $li_rightDepth<1 ? 1+$li_leftDepth : 1+$li_rightDepth);
    }
    

}