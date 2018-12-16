class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        from functools import reduce
        from math import gcd
        return True if reduce(math.gcd, Counter(deck).values()) > 1 else False

if __name__ == '__main__':
    s = Solution()
    l = [1]
    ret = s.hasGroupsSizeX(l)
    print(ret)