class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        res = 0
        for p0 in points:
            distmap = defaultdict(int)
            for p2 in points:
                dist = (p0[0] - p2[0]) ** 2 + (p0[1] - p2[1]) ** 2
                distmap[dist] += 1
            for p in distmap:
                res += distmap[p] * (distmap[p] - 1)
        return res