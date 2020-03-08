# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        depth = 0
        result = []
        while queue:
            length = len(queue)
            sub_queue = []
            for i in range(length):
                node = queue.pop(0)
                if (depth % 2 == 0):
                    sub_queue.append(node.val)
                else:
                    sub_queue.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            result.append(sub_queue)
        return result
                
        