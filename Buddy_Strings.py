class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        from collections import Counter
        difference, s = 0, []
        if len(A) != len(B):
            return False
        elif A == B:
            c = Counter(A)
            if any(x >= 2 for x in c.values()):
                return True
            else:
                return False
        else:
            if Counter(A) != Counter(B):
                return False
            for ch1, ch2 in zip(A, B):
                if difference > 2:
                    break
                if ch1 != ch2:
                    difference += 1
            return difference == 2