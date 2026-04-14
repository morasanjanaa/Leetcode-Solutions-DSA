class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        l1 = list(s)

        for i in range(len(l1)):
            if l1[i] == "(":
                stack.append(i)

            elif l1[i] == ")":
                start = stack.pop()
                l1[start + 1:i] = l1[start + 1:i][::-1]

        result = []
        for ch in l1:
            if ch != "(" and ch != ")":
                result.append(ch)

        return "".join(result)