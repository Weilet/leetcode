class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left, right = left + 1, right - 1
        one, two = s[:left] + s[left+1:], s[:right] + s[right+1:]
        return one == one[::-1] or two == two[::-1]