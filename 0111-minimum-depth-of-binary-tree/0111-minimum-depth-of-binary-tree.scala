/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def minDepth(root: TreeNode): Int = {
        if(root == null) return 0
        helper(List(root))
    }
    
    def helper(list: List[TreeNode]): Int = {
        if(list.isEmpty) return 0
        if(list.exists(o => o.left == null && o.right == null)) 1
        else helper(list.flatMap(o => List(o.left, o.right).filterNot(_ == null))) + 1
    }
}