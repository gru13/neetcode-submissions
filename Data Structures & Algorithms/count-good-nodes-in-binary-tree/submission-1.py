# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def solve(node, max_):
            nonlocal count
            if node is None:
                return
            if max_ <= node.val:
                max_ = node.val
                count += 1
            solve(node.left, max_)
            solve(node.right, max_)
    
        solve(root, root.val)
        return count