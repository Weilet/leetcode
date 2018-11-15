class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


if __name__ == '__main__':
    s = Solution()
    ret = s.judgeCircle("UDURDDLL")
    print(ret)