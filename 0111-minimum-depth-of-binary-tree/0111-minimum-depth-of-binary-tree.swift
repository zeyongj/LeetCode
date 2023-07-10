# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def min_depth(root)
    return 0 if !root
    l,r = min_depth(root.left), min_depth(root.right)
    1 + ((l==0 or r==0) ? l+r : [l,r].min) 
end