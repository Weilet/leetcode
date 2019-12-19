class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindromic(subs):
            return subs == subs[::-1]
        cnt = len(s)
        for i in range(2, len(s)+1):
            for j in range(len(s) - i + 1):
                if is_palindromic(s[j:j+i]):
                    cnt += 1
        return cnt

# Manacher's algorithm awaiting adaption
