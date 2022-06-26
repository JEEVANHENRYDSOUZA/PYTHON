class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False # all negative numbers are not pallindrome in nature
        
        
        elif x == 0:
            return True
        x = str(x)
        lmost = 0
        rmost = len(x)-1
        while lmost <= rmost:
            if x[lmost] != x[rmost]:
                return False
            else:
                lmost += 1
                rmost -= 1
        return True
