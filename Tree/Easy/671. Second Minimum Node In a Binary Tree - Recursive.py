# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        left = root.left.val
        right = root.right.val
        if left == root.val:
            left = self.findSecondMinimumValue(root.left)
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)
        if left != -1 and right != -1:
            return min(left, right)
        elif left != -1:
            return left
        else:
            return right

            
            
        

        