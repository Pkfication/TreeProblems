# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        def recMaxLevel(root, level):
            if root:
                if len(self.levels) == level:
                    self.levels.append([])
                self.levels[level].append(root.val)
                if root.left:
                    recMaxLevel(root.left, level+1)
                if root.right:
                    recMaxLevel(root.right, level+1)
        
        if not root:
            return None
        self.levels = []
        recMaxLevel(root, 0)
        high = sum(self.levels[0])
        level = 1
        for i,v in enumerate(self.levels):
            s = sum(v)
            if s > high:
                high = s
                level = i + 1
        return level
