class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for ch in s.strip()[::-1]:
            if ch != ' ':
                res += 1
            else:
                break
        return res
