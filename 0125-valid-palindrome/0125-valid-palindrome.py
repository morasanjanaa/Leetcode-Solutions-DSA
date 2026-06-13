class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = s.lower()
        t = ""
        for i in p:
            if i.isalnum():
                t += i
        left=0
        right=len(t)-1
        while(left<=right):
            if t[left] == t[right]:
                left+=1
                right-=1
            else:
                return False
        return True


       

        