# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traversal(root, result)
        return result
    
    def traversal(self, node, result):
        if node:
            self.traversal(node.left, result)
            result.append(node.val)
            self.traversal(node.right, result)
        
        