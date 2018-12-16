class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        times = math.ceil(len(B) / len(A))
        string = A * times
        if string.count(B) <= 0:
            string += A
            times += 1
        if string.count(B) <= 0:
            string = A + string
            times += 1
        if string.count(B) <= 0:
            return -1
        else:
            return times
