class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            time = n // i
            temp = s[:i] * time
            if temp == s:
                return True
        return False