class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        keymap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre = s[0]
        for ch in s:
            if keymap[ch] > keymap[pre]:
                res -= 2 * keymap[pre]
            res += keymap[ch]
            pre = ch
        return res
