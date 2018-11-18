class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = ''
        for i in range(len(bin(num))-2):
            x += '1'
        num = num ^ int(x, 2)
        return num
