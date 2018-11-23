class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(S)):
            forward, backward = 0, 0
            while True:
                if S[i+forward] == C:
                    ans.append(forward)
                    break
                elif i+forward < len(S)-1:
                    forward += 1
                if S[i-backward] == C:
                    ans.append(backward)
                    break
                elif i-backward >= 1:
                    backward += 1
        return ans
