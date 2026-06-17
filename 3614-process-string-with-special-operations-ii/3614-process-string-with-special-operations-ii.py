class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Length of the string after each operation
        lengths = [0]

        for ch in s:
            cur = lengths[-1]

            if ch.isalpha():
                cur += 1
            elif ch == "*":
                if cur > 0:
                    cur -= 1
            elif ch == "#":
                cur *= 2
            elif ch == "%":
                pass  # length unchanged

            lengths.append(cur)

        if k >= lengths[-1]:
            return '.'

        # Work backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur = lengths[i + 1]
            prev = lengths[i]

            if ch.isalpha():
                if k == prev:
                    return ch

            elif ch == "*":
                # Before '*', one extra character existed at the end.
                pass

            elif ch == "#":
                half = prev
                if k >= half:
                    k -= half

            elif ch == "%":
                if prev > 0:
                    k = prev - 1 - k

        return '.'