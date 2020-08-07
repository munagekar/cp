def prep(node, x, y, m):
    if not node:
        return

    m[x].append((y, node.val))

    prep(node.left, x - 1, y + 1, m)
    prep(node.right, x + 1, y + 1, m)


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        mapi = collections.defaultdict(list)
        prep(root, 0, 0, mapi)

        res = []
        for _, l in sorted(mapi.items()):
            res.append([x for _, x in sorted(l)])
        return res