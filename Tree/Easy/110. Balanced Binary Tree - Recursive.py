# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def countNode(root):
            if (not root):
                return 0
            return 1 + max(countNode(root.left), countNode(root.right))
        
        if (not root):
            return True
        return (abs(countNode(root.left) - countNode(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

