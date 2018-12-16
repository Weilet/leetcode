class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import itertools

        def area(p, q, r):
            return .5 * abs(p[0]*q[1] + q[0]*r[1] + r[0]*p[1]
                         - p[0]*r[1] - q[0]*p[1] - r[0]*q[1])
        return max(area(*triangle) for triangle in itertools.combinations(points, 3))
