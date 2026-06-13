# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_deep = 0
        def solve(node):
            if node is None:
                return 0

            nonlocal max_deep
            cur_right_depth = solve(node.right) 
            cur_left_depth = solve(node.left)
            max_deep = max(cur_right_depth+cur_left_depth, max_deep)
            return max(cur_right_depth, cur_left_depth) + 1
        
        solve(root)
        return max_deep
        