class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        ans = [''] * len(words)
        for i, word in enumerate(words, start=1):
            if word[0].lower() in 'aeiou':
                ans[i] = word + 'ma' + 'a' * i
            else:
                ans[i] = word[1:] + word[0] + 'ma' + 'a' * i
        return " ".join(ans)
