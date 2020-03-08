# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.set = set()
        self.traverse(root)
        return len(self.set) == 1
        
    def traverse(self, node):
        if not node:
            return
        self.set.add(node.val)
        self.traverse(node.left)
        self.traverse(node.right)

            
        