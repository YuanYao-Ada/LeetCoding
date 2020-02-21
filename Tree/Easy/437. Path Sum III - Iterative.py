# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        stack = [(root, [root.val])]
        result = 0
        while stack:
            node, values = stack.pop()
            result += values.count(sum)
            if node.left:
                stack.append((node.left, [x + node.left.val for x in values] + [node.left.val]))
            if node.right:
                stack.append((node.right, [x + node.right.val for x in values] + [node.right.val]))
        return result
        