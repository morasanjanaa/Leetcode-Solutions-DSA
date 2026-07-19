class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        def convert_int(s):
            ans = 0
            for i in s:
                ans = ans*10 + ord(i) - ord("0")
            return ans

        def convert_string(s):
            ans = ""
            while(s>0):
                last = s%10
                ans = chr(ord('0')+last)+ans
                s //= 10
            return ans

        def multiplyString(n1,n2):
            return convert_string(convert_int(n1)*convert_int(n2))

        return multiplyString(num1,num2)
