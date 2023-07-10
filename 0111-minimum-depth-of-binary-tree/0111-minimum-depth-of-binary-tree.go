/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
 func minDepth(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }
    var depth = 0
    var queue = [root]
    
    while !queue.isEmpty {
        var level = [TreeNode]()
        depth += 1
        
        for node in queue {
            if node.left == nil && node.right == nil {
                return depth
            }
         
            if let leftChild = node.left {
                level.append(leftChild)

            }
            
            if let rightChild = node.right {
                level.append(rightChild)
            }
            
        }
        queue = level
    }
    
    return depth
    
    }

}