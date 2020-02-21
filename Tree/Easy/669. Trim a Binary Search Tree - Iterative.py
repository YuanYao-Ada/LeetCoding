# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root and not(L <= root.val <= R):
            if root.val < L:
                root = root.right 
            if root.val > R:
                root = root.left 
        stack = [root]
        while stack:
            node = stack[-1]
            if not node:
                stack.pop()
                continue
            update = 0
            if node.left and node.left.val < L:
                node.left = node.left.right
                update += 1
            if node.right and node.right.val > R:
                node.right = node.right.left
                update += 1
            if not update:
                stack.pop()
                stack.append(node.left)
                stack.append(node.right)
        return root
        