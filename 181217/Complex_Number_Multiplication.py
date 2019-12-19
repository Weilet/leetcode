class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a.split('+')[0])
        y = int(a.split('+')[1][:-1])
        c = int(b.split('+')[0])
        d = int(b.split('+')[1][:-1])
        return str(c * x - d * y) + '+' + str(d * x + c * y) + 'i'
