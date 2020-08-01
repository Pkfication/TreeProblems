# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        elems = []
        self.recursivePreorderTraversal(root, elems)
        return elems
        
    def recursivePreorderTraversal(self, root, elems):
        if root:
            elems.append(root.val)
            self.recursivePreorderTraversal(root.left, elems)
            self.recursivePreorderTraversal(root.right, elems)
        
