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

        levels = []
        q = [(root, 0)]
        while len(q):
            cur = q.pop(0)

            cur_item = cur[0]
            cur_level = cur[1]

            if cur_item.left is not None:
                q.append((cur_item.left, cur_level+1))

            if cur_level >= len(levels):
                levels.append([])
            levels[cur_level].append(cur_item.val)

            if cur_item.right is not None:
                q.append((cur_item.right, cur_level+1))

        return levels