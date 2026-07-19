class Solution:
    def getHint(self, secret: str, hidden: str) -> str:
            bulls = 0
            cows = 0
            sc_dict = {}
            hi_dict = {}

            for i in range(len(secret)):
                if secret[i] == hidden[i]:
                    bulls += 1
                else:
                    if secret[i] in sc_dict:
                        sc_dict[secret[i]] += 1
                    else:
                        sc_dict[secret[i]] = 1
                    if hidden[i] in hi_dict:
                        hi_dict[hidden[i]] += 1
                    else:
                        hi_dict[hidden[i]] = 1
                        
            for digit in sc_dict:
                if digit in hi_dict:
                    cows += min(sc_dict[digit],hi_dict[digit])
            return str(bulls)+"A"+str(cows)+"B"

        