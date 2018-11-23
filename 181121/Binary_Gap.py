import re
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        return max(len(x) for x in bin(N)[2:].strip('0').split('1'))+1 if N & N-1 else 0


if __name__ == '__main__':
    s = Solution()
    ret = s.binaryGap(8)
    print(ret)