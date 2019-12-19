class Solution(object):
    def constructArray(self, n, k):
        ret = []
        nums = range(1, n + 1)
        seen = [False] * (n + 1)
        for x in nums:
            if not seen[x]:
                ret.append(x)
                seen[x] = True
            if not seen[k+2-x] and k+2-x > 0:
                ret.append(k+2-x)
                seen[k+2-x] = True
        return ret
