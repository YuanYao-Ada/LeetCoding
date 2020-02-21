# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(treenode1, treenode2):
            if (treenode1 is None and treenode2 is None):
                return True
            if (treenode1 is None or treenode2 is None):
                return False
            return treenode1.val == treenode2.val and isMirror(treenode1.left, treenode2.right)
            and isMirror(treenode1.right, treenode2.left)
        
        return isMirror(root, root)
        
        