class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        stack = [TreeNode(pre[0])]

        postc = 0
        for val in pre[1:]:
            node = TreeNode(val)
            while stack[-1].val == post[postc]:
                postc += 1
                stack.pop()

            if not stack[-1].left:
                stack[-1].left = node

            else:
                stack[-1].right = node

            stack.append(node)

        return stack[0]


class Solution2:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        prec = 0
        postc = 0

        def helper():
            nonlocal prec
            nonlocal postc

            root = TreeNode(pre[prec])
            prec += 1

            if root.val != post[postc]:
                root.left = helper()

            if root.val != post[postc]:
                root.right = helper()

            postc += 1
            return root

        return helper()