class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(sum([ord(x) for x in t]) - sum([ord(x) for x in s]))