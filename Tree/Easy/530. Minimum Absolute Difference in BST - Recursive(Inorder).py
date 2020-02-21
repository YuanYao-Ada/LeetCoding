# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def fn(node, low, high):
            if not node: 
                return high - low
            left = fn(node.left, low, node.val)
            right = fn(node.right, node.val, high)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))
        