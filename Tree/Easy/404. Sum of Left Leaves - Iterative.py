# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if node.right.left or node.right.right:
                    stack.append(node.right)
        return result
            
            
        