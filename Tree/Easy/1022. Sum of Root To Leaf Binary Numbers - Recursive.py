# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.sumRoot(root)
    
    def sumRoot(self, node, val=0):
        if not node:
            return 0
        val = val*2 + node.val
        if not node.left and not node.right:
            return val
        return self.sumRoot(node.left, val) + self.sumRoot(node.right, val)
                
                
            
        