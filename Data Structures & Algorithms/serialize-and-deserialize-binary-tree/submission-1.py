from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        if not root:
            return "None"

        result = []
        q = deque([root])

        while q:
            cur = q.popleft()

            if cur is None:
                result.append("None")
            else:
                result.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)

        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        values = data.split(",")

        if values[0] == "None":
            return None

        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1

        while q and i < len(values):
            cur = q.popleft()

            # Left child
            if i < len(values) and values[i] != "None":
                cur.left = TreeNode(int(values[i]))
                q.append(cur.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != "None":
                cur.right = TreeNode(int(values[i]))
                q.append(cur.right)
            i += 1

        return root