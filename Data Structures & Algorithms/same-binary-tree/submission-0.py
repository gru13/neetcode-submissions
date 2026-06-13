# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(nodeA, nodeB):
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                return False
            
            if nodeA.val != nodeB.val:
                return False
            
            left_result = solve(nodeA.left, nodeB.left)
            right_result = solve(nodeA.right, nodeB.right)
             
            return True and left_result and right_result
        return solve(p, q)