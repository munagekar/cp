# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        val = []

        def helper(n):
            if not n:
                return
            val.append(n.val)
            helper(n.left)
            helper(n.right)

        helper(root)
        return " ".join((str(v) for v in val))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals = [int(v) for v in data.split(" ")]
        vals = collections.deque(vals)

        def helper(mini, maxi):
            if vals and mini <= vals[0] <= maxi:
                v = vals.popleft()
                node = TreeNode(v)
                node.left = helper(mini, v)
                node.right = helper(v, maxi)

                return node

        return helper(-1, 10 ** 5)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans