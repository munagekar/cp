def solve(root, solution, level):
    if not root:
        return
    try:
        solution[level].append(root.val)
    except:
        solution.append([root.val])

    solve(root.left, solution, level + 1)
    solve(root.right, solution, level + 1)


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        solution = []
        solve(root, solution, 0)
        return solution[::-1]