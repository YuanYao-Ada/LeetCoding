# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, root.val, 0)]
        result = []
        while queue:
            node, value, level = queue.pop(0)
            if not node.left and not node.right:
                result.append(value)
            if node.left:
                queue.append((node.left, value * 2 + node.left.val, level + 1))
            if node.right:
                queue.append((node.right, value * 2 + node.right.val, level + 1))
        print(result)
        return sum(result)
                
                
            
        