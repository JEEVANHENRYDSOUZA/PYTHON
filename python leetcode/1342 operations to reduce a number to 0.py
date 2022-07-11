class Solution(object):
    def numberOfSteps(self, num):
        steps=0
        binary=bin(num)[2:]
        for i in binary:
            if i=="1":
                steps=steps+2
            if i=="0":
                steps=steps+1
        return steps -1
