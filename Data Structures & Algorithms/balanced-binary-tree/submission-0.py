# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def solve(node):    

            nonlocal balanced

            if node is None:
                return 1
            
            l_d = solve(node.left)
            r_d = solve(node.right)

            if abs(l_d-r_d) > 1:
                balanced = False

            return 1 + max(l_d,  r_d)

        solve(root)

        return balanced
