# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.prev = None
        self.max_count = 0
        self.current_count = 0
        self.result = []
        
        def search(node):
            if not node:
                return
            search(node.left)
            self.current_count = 1 if node.val != self.prev else self.current_count + 1
            if self.current_count == self.max_count:
                self.result.append(node.val)
            elif self.current_count > self.max_count:
                self.result = [node.val]
                self.max_count = self.current_count
            self.prev = node.val

            search(node.right)
        search(root)
        return self.result
        
        
                    

        