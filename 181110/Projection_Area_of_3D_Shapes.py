class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(val != 0 for row in grid for val in row) + sum(max(row) for row in grid) + sum(max(row[i] for row in grid) for i in range(len(grid)))


if __name__ == '__main__':
    s = Solution()
    l = [[1,0],[0,2]]
    ret = s.projectionArea(l)
    print(ret)