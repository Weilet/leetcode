class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, tmp = 0, 2
        for i in range(1, len(S)):
            if S[i] == '(':
                tmp *= 2
            else:
                tmp //= 2
                if S[i-1] == '(':
                    res += tmp
        return res