class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        high, low = len(S), 0
        for x in S:
            if x == 'D':
                ans.append(high)
                high -= 1
            else:
                ans.append(low)
                low += 1
        return ans + [low]
