# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        if root.left:
            if (not root.left.left and not root.left.right):
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)
        if root.right:
            if root.right.left or root.right.right:
                result += self.sumOfLeftLeaves(root.right)
        return result
        
            
            
        