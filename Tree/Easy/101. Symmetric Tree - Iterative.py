# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [root.left, root.right]
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if (node1 is None and node2 is None):
                continue
            if (node1 is None or node2 is None or node1.val != node2.val):
                return False
            stack = [node1.left, node2.right, node1.right, node2.left] + stack
        return True

