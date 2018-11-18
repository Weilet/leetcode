import functools
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t = x ^ y
        r = functools.reduce(lambda cnt, a: cnt + 1 if a == '1' else cnt, bin(t), 0)
        return r
        