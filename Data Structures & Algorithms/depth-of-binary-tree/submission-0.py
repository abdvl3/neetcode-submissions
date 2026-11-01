# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

      #when you get to a node, calculate 1 + the max of depth of left and right subtree depth  
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))