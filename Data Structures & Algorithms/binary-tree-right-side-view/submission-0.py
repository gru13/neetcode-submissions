# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layers = {}
        def solve(node, deep):
            if node is None:
                return 
            if deep not in layers.keys():
                layers[deep] = []
            solve(node.left, deep+1)
            layers[deep].append(node.val)
            solve(node.right, deep+1)
        
        solve(root, 0)
        print(layers)
        return [a[-1] for a in layers.values()]