class Solution(object):
    def findLUSlength(self, a, b):
        """
        :param: a, b
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))
