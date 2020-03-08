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
        stack = [(root, lower, higher)]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        return True

