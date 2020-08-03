# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxDepth = 0
        self.depth(root, 1)
        return self.maxDepth
        
    def depth(self, root, depth):
        if not root:
            return None
        
        if not root.left and not root.right:
            self.maxDepth = max(depth, self.maxDepth)
        
        self.depth(root.left, depth+1)
        self.depth(root.right, depth+1)