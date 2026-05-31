class Solution:
    def reverse(self, x: int) -> int:
        y=str(abs(x))
        sum=0
        for i in range(len(y)):
            sum+= int(y[i]) * (10**i)
        
        if sum < -2**31 or sum > 2**31 - 1:
            return 0

        if x<0:
            return -sum
        else:
            return sum