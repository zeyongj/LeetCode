/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    
    if (root == null) return 0;
    
    let min = Number.MAX_SAFE_INTEGER;
    
    findMin(root, 1);
    
    return min;
    
    function findMin(node, depth) {
        // base
        if (node == null) return 0;
        
        if (node.left == null && node.right == null) {
            min = Math.min(min, depth);
        }
        
        findMin(node.left, depth + 1);
        findMin(node.right, depth + 1);
    }
};