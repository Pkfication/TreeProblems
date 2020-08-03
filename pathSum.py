# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.answer = False
        self.recPathSum(root, 0, sum)
        return self.answer
        
    def recPathSum(self, root, csum, sum: int):
        if not root:
            return None
        
        csum += root.val
        if not root.left and not root.right:
            if not self.answer:
                self.answer = csum == sum
            
        self.recPathSum(root.left, csum, sum)
        self.recPathSum(root.right, csum, sum)
