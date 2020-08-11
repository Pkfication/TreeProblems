# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return None
        
        h_sum = root.val
        q = [root]
        c_l = 0
        h_l = 0
        while q:
            tmp = []
            s = 0
            c_l += 1
            while q:
                node = q.pop(0)
                s += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if s > h_sum:
                h_sum = s
                h_l = c_l
            if tmp:
                q = tmp
        return h_l
