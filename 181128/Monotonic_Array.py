class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(x > y for x, y in zip(A, A[1:])) or all(x < y for x, y in zip(A, A[1:]))