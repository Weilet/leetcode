class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF  # 这两个
        MASK = 0xFFFFFFFF  # 是关键
        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)   
