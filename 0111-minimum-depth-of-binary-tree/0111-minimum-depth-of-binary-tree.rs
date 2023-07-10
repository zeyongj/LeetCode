/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun minDepth(root: TreeNode?): Int = with(ArrayDeque<TreeNode>()) {
      root?.let { add(it) }
      generateSequence(1) { (it + 1).takeIf { isNotEmpty() } }
        .firstOrNull {
          (1..size).any {
            with(poll()) {
              left?.let { add(it) }
              right?.let { add(it) }
              left == null && right == null
            }
          }
        } ?: 0
    }
}