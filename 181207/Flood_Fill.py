class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def paint(i, j):
            if image[i][j] == color:
                image[i][j] = newColor
            for offset in offsets:
                if 0 <= i+offset[0] < len(image) \
                    and 0 <= j+offset[1] < len(image[0]) \
                        and image[i+offset[0]][j+offset[1]] == color \
                        and image[i+offset[0]][j+offset[1]] != newColor :
                    paint(i+offset[0], j+offset[1])

        paint(sr, sc)
        return image