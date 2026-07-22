class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        size = n-k
        window_sum = sum(cardPoints[:size])
        min_sum = window_sum

        for i in range(size,n):
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i-size]
            min_sum = min(window_sum,min_sum)
        
        return total - min_sum









        '''
        total = sum(cardPoints)
        n = len(cardPoints)-k

        min_window_sum = sum(cardPoints[0:n])
        window_sum = min_window_sum

        for i in range(n,len(cardPoints)):
            window_sum -= cardPoints[i-n]
            window_sum += cardPoints[i]
            min_window_sum = min(window_sum,min_window_sum)

        return total - min_window_sum
        '''
        



        
