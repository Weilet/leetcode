class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def inside(pos, lim):
            return 0 <= pos < lim
        ans = 0
        x, y, n = 0, 1, len(grid)
        offsets =[[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:
                    continue
                ans += 4 * val + 2
                for offset in offsets:
                    if inside(j+offset[x], n) and inside(i+offset[y], n):
                        ans -= min(val, grid[i+offset[y]][j+offset[x]])
        return ans
