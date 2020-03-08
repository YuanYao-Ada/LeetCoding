# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.result1 = []
        self.result2 = []
        self.bfs(root1, self.result1)
        self.bfs(root2, self.result2)
        return self.result1 == self.result2
        
        
    def bfs(self, node, result):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.val)
        self.bfs(node.left, result)
        self.bfs(node.right, result)
            
                
        