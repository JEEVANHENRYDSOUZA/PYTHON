class Solution:
    def isPowerOfTwo(self, n):
        while(n>=2):
            if(n%2!=0):
                return False
            else:
                n=n/2
        return n==1
        
