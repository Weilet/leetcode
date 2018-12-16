class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c = {}
        for x in magazine:
            if x in c:
                c[x] += 1
            else:
                c[x] = 1
        for x in ransomNote:
            if c[x] > 0:
                c[x] -= 1
            else:
                return False
        return True
