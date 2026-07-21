class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s1):
            ans = []
            for i in s1:
                if i == "#":
                    if len(ans )== 0:
                        continue
                    ans.pop()
                else:
                    ans.append(i)
            return "".join(ans)
        return backspace(s) == backspace(t)
            

       