"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            queue = []
            if node.children:
                for child in node.children:
                    queue.insert(0, child)
                stack += queue
        return result
        