# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack1 = [root]
        stack2 = [1]
        result = 0
        while stack1:
            node = stack1.pop()
            value = stack2.pop()
            result = max(value, result)
            if node.left:
                stack1.append(node.left)
                stack2.append(value + 1)
            if node.right:
                stack1.append(node.right)
                stack2.append(value + 1)
        return result


        
