class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node is None:
                return
            
            if node == p or node == q:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        
        return helper(root)
