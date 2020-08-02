# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        ans = [[root.val]]
        while q:
            nodes = []
            tmp_nodes = []
            while q:
                curr = q.pop(0)
                if curr.left:
                    nodes.append(curr.left)
                    tmp_nodes.append(curr.left.val)
                if curr.right:
                    nodes.append(curr.right)
                    tmp_nodes.append(curr.right.val)
            q = nodes
            if tmp_nodes:
                ans.append(tmp_nodes)
        
        return ans
