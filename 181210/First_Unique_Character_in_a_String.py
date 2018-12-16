class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import OrderedDict
        d = OrderedDict()
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        for x in d:
            if d[x] == 1:
                return s.index(x)
        return -1
