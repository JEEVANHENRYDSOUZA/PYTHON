class Solution:
    def isPowerOfThree(self, n):
        while(n>=3):
            if(n%3!=0):
                return False
            else:
                n=n/3
        return n==1
        
