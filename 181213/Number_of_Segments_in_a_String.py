class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cnt = 0, 0
        for ch in s:
            if ch != ' ':
                cnt += 1
            else:
                res += 1 if cnt > 0 else 0
                cnt = 0
        res += 1 if cnt > 0 else 0
        return res
