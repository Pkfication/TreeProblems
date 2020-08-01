# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        self.recInorder(root, nodes)
        return nodes
        
    def recInorder(self, root: TreeNode, nodes):
        if root:
            self.recInorder(root.left, nodes)
            nodes.append(root.val)
            self.recInorder(root.right, nodes)
