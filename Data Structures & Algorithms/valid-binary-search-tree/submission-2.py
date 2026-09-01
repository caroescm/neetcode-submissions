# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        curr = root

        while curr:
            if curr.left is None:
                if prev is not None and curr.val <= prev:
                    return False
                prev = curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    pred.right = curr 
                    curr = curr.left
                else:
                    pred.right = None 
                    if prev is not None and curr.val <= prev:
                        return False
                    prev = curr.val
                    curr = curr.right

        return True