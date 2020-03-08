# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(result, root, 0)
        return result
    
    def helper(self, result, node, height):
        if not node:
            return
        if (height >= len(result)):
            result.append([])
        if (height % 2 == 0):
            result[height].append(node.val)
        else:
            result[height].insert(0, node.val)
        self.helper(result, node.left, height+1)
        self.helper(result, node.right, height+1)
        