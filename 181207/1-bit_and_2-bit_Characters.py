class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        pos = 0
        while pos < len(bits):
            if bits[pos] == 1:
                pos += 2
            else:
                bits[pos] += 1
        return pos == len(bits)

