# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.helper(self.result, root, 0)
        return self.result
    
    def helper(self, result, node, depth):
        if not node:
            return
        if (depth >= len(result)):
            result.append([])
        result[depth].append(node.val)
        self.helper(result, node.left, depth+1)
        self.helper(result, node.right, depth+1)

        
        