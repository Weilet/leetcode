class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = ['']
        for letter in S:
            if letter.isalpha():
                ans = [i + j for i in ans for j in [letter.upper(), letter.lower()]]
            else:
                ans = [i + letter for i in ans]
        return ans
        """
            shorter vision:
            L = [[ch.upper(), ch.lower()] if ch.isalpha() else ch for ch in S]
            return [''.join(ch) for ch in itertools.product(*L)]
        """