# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def solve(node):
            nonlocal max_sum
            if node is None:
                return 0
            
            sum_lft = max(0, solve(node.left))
            sum_ryt = max(0, solve(node.right))
            max_sum = max(max_sum, node.val + sum_lft + sum_ryt)
            return node.val + max(sum_lft, sum_ryt)
            
        solve(root)
        return max_sum