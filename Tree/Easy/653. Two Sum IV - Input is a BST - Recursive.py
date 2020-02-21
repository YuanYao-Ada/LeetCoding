# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        set1 = set()
        return self.traverse(root, k, set1)
    
    def traverse(self, node, k, set1):
        if not node:
            return False
        if k - node.val in set1:
            return True
        set1.add(node.val)
        return self.traverse(node.left, k, set1) or self.traverse(node.right, k, set1)
        
        
        