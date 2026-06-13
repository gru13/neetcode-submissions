# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            the basic idea is to do a dfs or bfs and reach the deepest node and then check which has more
            in dfs we will use stack or queue with (node, depth) 
        """        
        def depth(node):
            if node == None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        
        return depth(root)
