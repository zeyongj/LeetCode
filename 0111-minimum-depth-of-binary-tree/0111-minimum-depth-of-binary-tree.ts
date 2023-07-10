/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function minDepth(root: TreeNode | null): number {
    if (!root) return 0;
    
    return minDepthHelper(root, 0);
    // T.C: O(N)
    // S.C: O(H)
};

function minDepthHelper(node: TreeNode | null, prevDepth: number): number {
    if (!node) return Infinity;
    if (!node.left && !node.right) return prevDepth + 1;
    
    return Math.min(minDepthHelper(node.left, prevDepth + 1), minDepthHelper(node.right, prevDepth + 1));
}