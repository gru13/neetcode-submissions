# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = defaultdict(list)
        def traverse(node, deep):
            if node is None:
                return
            traverse(node.left, deep+1)
            levels[deep].append(node.val)
            traverse(node.right, deep+1)


        traverse(root, 0)
        return [a[-1] for a in sorted(levels.items(), key=lambda x:x[0])]