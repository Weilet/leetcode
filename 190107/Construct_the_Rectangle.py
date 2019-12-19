import  math
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        res = []
        i = math.floor(math.sqrt(area))
        while True:
            if area % i == 0:
                res.append(area // i)  # 长宽不能反，不愧是差评题目
                res.append(i)
                break
            i -= 1
        return res
    