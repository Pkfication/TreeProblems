# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        self.recPostorder(root, nodes)
        return nodes
        
    def recPostorder(self, root:TreeNode, nodes):
        if root:
            self.recPostorder(root.left, nodes)
            self.recPostorder(root.right, nodes)
            nodes.append(root.val)
            
