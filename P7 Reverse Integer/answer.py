class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        r = int(s[::-1])
        if x == 0:
            return x
        elif (r > 2 ** 31 - 1) or (r < -1 * 2 **31):
            return 0
        elif x > 0:
            return r
        else:
            return -1 * r
