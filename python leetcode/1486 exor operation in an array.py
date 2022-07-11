class Solution:
    def xorOperation(self, n, start):
        exor=0
        array=[]
        for i in range(0,n):
            array.append(start+2*i)
        for j in array:
            exor=exor^j
            
        return exor
