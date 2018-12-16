class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ''
        for ch in s.lower():
            if ch.isalpha() or ch.isnumeric():
                new_string += ch
        return new_string == new_string[::-1]