class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vch = 'aeiouAEIOU'
        v = []
        pos = []
        for i, ch in enumerate(s):
            if ch in vch:
                v.append(ch)
                pos.append(i)
        for x in pos:
            s[x] = v.pop()
        return ''.join(s)
