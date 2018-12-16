class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = sum(A) - sum(B)
        A = set(A)
        # if you use other variable to save "set(A)",
        # the time this code's execution would decrease a little
        for y in B:
            if diff/2 + y in A:
                return [diff/2 + y, y]