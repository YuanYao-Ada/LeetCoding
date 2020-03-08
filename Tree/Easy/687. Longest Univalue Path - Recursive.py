# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        
        def postOrder(node):
            if not node:
                return 0
            left = postOrder(node.left)
            right = postOrder(node.right)
            left_result = 0
            right_result = 0
            if node.left and node.left.val == node.val:
                left_result = left + 1
            if node.right and node.right.val == node.val:
                right_result = right + 1
            self.result = max(self.result, left_result + right_result)
            return max(left_result, right_result)
        postOrder(root)
        return self.result
        
        