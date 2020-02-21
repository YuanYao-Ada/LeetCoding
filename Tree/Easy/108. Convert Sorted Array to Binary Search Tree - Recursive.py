# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sortedArray(nums, left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            current = TreeNode(nums[mid])
            current.left = sortedArray(nums, left, mid-1)
            current.right = sortedArray(nums, mid+1, right)
            return current
        
        return sortedArray(nums, 0, len(nums)-1)
        

