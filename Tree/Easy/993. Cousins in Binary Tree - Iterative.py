# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        if root.val == x or root.val == y:
            return False
        queue = [(root, None, 0)]
        result = []
        while queue:
            node, parent, level = queue.pop(0)
            if node.left:
                if node.left.val == x or node.left.val == y:
                    result.append((node.val, level+1))
                queue.append((node.left, node.val, level+1))
            if node.right:
                if node.right.val == x or node.right.val == y:
                    result.append((node.val, level+1))
                queue.append((node.right, node.val, level+1))
        return result[0][0] != result[1][0] and result[0][1] == result[1][1]
        
                
            
            
        