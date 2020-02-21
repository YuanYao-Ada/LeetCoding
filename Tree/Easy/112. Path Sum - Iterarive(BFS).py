# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            current, value = queue.pop(0)
            if not current.left and not current.right:
                if value == sum:
                    return True
                
            if current.left:
                queue.append((current.left, value + current.left.val))
            if current.right:
                queue.append((current.right, value + current.right.val))
                
        return False

            
        