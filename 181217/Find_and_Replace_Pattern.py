class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            P = {}
            for x, y in zip(word, pattern):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())
        return list(filter(match, words))
# two map solution also works