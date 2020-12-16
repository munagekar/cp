def cal(op, l):
    if op == "!":
        return not l[0]

    if op == "|":
        return any(l)

    if op == "&":
        return all(l)


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        e = expression.strip()

        # Commas dont provide any value
        e = e.replace(",", "")

        stack = []

        for c in e:
            if c == "t":
                stack.append(True)
            elif c == "f":
                stack.append(False)
            elif c == "&":
                stack.append("&")
            elif c == "|":
                stack.append("|")
            elif c == "!":
                stack.append("!")
            elif c == "(":
                stack.append("(")
            else:
                # Items will only Contain Booleans
                items = []
                while True:
                    n = stack.pop()
                    if n == "(":
                        break
                    items.append(n)
                stack.append(cal(stack.pop(), items))

        return stack.pop()