class Solution:
    def reverse(self, num: int) -> int:
        is_neg = False
        if num < 0:
            is_neg = True
            num *= -1
        temp = 0
        while(num != 0):
            temp = temp * 10 + num % 10
            num //= 10
        if temp > (2 ** 31)-1 or temp < (-2 ** 31):
            return 0
        return temp * -1 if is_neg == True else temp
        







        
        '''
        is_neg = False
        if(x<0):
            is_neg = True
            x *=-1
        ans = 0
        while(x>0):
            y = x%10
            ans = ans*10 + y
            x = x//10
        if ans > 2 ** 31 - 1:
            return 0
        return ans * -1 if is_neg else ans
        '''

        
        