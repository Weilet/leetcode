class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ''
        from collections import Counter
        c = Counter(T)
        for ch in S:
            if ch in c:
                res += ch * c[ch]
                del c[ch]
        for ch in c:
            res += ch * c[ch]
        return res