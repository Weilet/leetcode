class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [x for x in range(left, right+1) if all(i != '0' and x % int(i) == 0 for i in str(x))]