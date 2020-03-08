# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.parent = {}
        self.depth = {}
        self.dfs(root)
        return self.parent[x] != self.parent[y] and self.depth[x] == self.depth[y]
        
    def dfs(self, node, parent=None):
        if not node:
            return
        self.depth[node.val] = 1 + self.depth[parent.val] if parent else 0
        self.parent[node.val] = parent
        self.dfs(node.left, node)
        self.dfs(node.right, node)
        
        
                
            
            
        