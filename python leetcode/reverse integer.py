class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        if x > 0:
            res = 0
            while x > 0:
                x, remain = divmod(x,10)
                res = 10 * res + remain
            if -2 ** 31 <= res <= 2 ** 31 - 1:
                return res
            else:
                return 0
        elif x < 0:
            x = -x
            res = 0
            while x > 0:
                x, remain = divmod(x,10)
                res = 10 * res + remain
            res = -res
            if -2 ** 31 <= res <= 2 ** 31 - 1:
                return res
            else:
                return 0
