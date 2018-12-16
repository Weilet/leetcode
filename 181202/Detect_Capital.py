class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return \
            all(ch.isupper() for ch in word) or \
            all(ch.islower() for ch in word) or \
            (word[0].isupper() and all(ch.islower() for ch in word[1:]))
