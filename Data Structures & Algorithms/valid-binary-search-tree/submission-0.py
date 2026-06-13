# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node, min_, max_):
            if node is None:
                return True

            if min_ < node.val < max_:
                return solve(node.left, min_, node.val) and solve(node.right, node.val, max_)
            else:
                return False
        return solve(root, float('-inf'), float('inf'))
