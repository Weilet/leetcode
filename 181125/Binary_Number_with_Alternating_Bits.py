class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return all(int(x)+int(y) == 1 for x, y in zip(bin(n)[2:], bin(n)[3:]))