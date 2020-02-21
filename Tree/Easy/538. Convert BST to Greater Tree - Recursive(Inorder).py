# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        return self.inorder(root)
        
    def inorder(self, root):
        if root:
            self.inorder(root.right)
            self.total += root.val
            root.val = self.total
            self.inorder(root.left)
            return root
            
        