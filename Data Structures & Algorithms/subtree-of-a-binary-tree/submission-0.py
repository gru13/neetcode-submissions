# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(nodeA, nodeB):
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                return False
            if nodeA.val != nodeB.val:
                return False
            return isEqual(nodeA.left, nodeB.left) and isEqual(nodeA.right, nodeB.right)
        
        if root is None:
            return False
        if isEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
