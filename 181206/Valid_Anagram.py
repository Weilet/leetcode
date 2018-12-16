class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        if len(s) != len(t):
            return False
        cs = Counter(s)
        ct = Counter(t)
        if cs == ct:
            return True
        else:
            return False