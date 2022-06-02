class Solution:
    def isPowerOfFour(self, n) :
        while(n>=4):
            if(n%4!=0):
                return False
            else:
                n=n/4
        return n==1
        
