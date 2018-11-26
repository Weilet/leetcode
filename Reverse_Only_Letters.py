import re
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = ""
        raws = "".join(re.findall(r'[a-zA-Z]*', S))
        pos = -1
        for x in S:
            if x.isalpha():
                ans += raws[pos]
                pos -= 1
            else:
                ans += x
