# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower = float('-inf')
        higher = float('inf')
        return self.helper(root, lower, higher)
    
    def helper(self, node, lower, higher):
        if not node:
            return True
        if node.val <= lower or node.val >= higher:
            return False
        if not self.helper(node.left, lower, node.val):
            return False
        if not self.helper(node.right, node.val, higher):
            return False
        return True
        