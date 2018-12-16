class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) <= 1:
            return False
        for i in range(len(A)):
            if A == B:
                return True
            A = A[1:] + A[0]
        return False