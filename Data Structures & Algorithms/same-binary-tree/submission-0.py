# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty -> match
        if not p and not q:
            return True
        
        # One empty, other not -> mismatch
        if not p or not q:
            return False
        
        # Values differ -> mismatch
        if p.val != q.val:
            return False
        
        # Recurse on left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)