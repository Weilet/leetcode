class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ans = []
        from collections import Counter
        a = Counter(A.split())
        b = Counter(B.split())
        for x in a:
            if a[x] == 1 and x not in b:
                ans.append(x)
        for x in b:
            if b[x] == 1 and x not in a:
                ans.append(x)
        return ans