class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        offsets =[[1, 0], [-1, 0], [0, 1], [0, -1]]

        def is_inside(num, n):
            return 0 <= num < n

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                side = 4
                for offset in offsets:
                    if is_inside(i+offset[0], len(grid[0])) and is_inside(j+offset[1], len(grid[0])):
                        if grid[i + offset[0]][j + offset[1]] == 1:
                            side -= 1
                ans += side
        return ans


if __name__ == '__main__':
    s = Solution()
    l = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    ret = s.islandPerimeter(l)
    print(ret)

#  TODO: speed up the code
