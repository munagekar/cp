class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        q = [(root, 1)]

        ans = []
        while q:
            n, p_flag = q.pop()
            if not p_flag:
                ans.append(n.val)
                continue
            if n.right:
                q.append((n.right, 1))
            q.append((n, 0))
            if n.left:
                q.append((n.left, 1))

        return ans
