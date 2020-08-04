# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        l = len(inorder)
        return self.treeBuilder(0, l - 1, 0, l - 1, inorder, postorder)
        
    def treeBuilder(self, postStart, postEnd, inStart, inEnd, inorder, postorder):
        if inStart > inEnd:
            return None
        
        root = TreeNode(postorder[postEnd])
        
        rootIndex = inorder.index(root.val)
        rightTreeSize = inEnd - rootIndex
        leftTreeSize =  rootIndex - inStart
        
        root.left = self.treeBuilder(postStart, postStart + leftTreeSize - 1, inStart, rootIndex - 1, inorder, postorder)
        root.right = self.treeBuilder(postEnd - rightTreeSize , postEnd - 1, rootIndex + 1, inEnd, inorder, postorder)
        
        return root
