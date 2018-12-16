class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum((ord(x)-64) * 26**(len(s) - i) for x, i in zip(s, range(1, len(s)+1)))