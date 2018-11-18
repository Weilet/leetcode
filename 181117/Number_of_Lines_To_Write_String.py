class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        hash_map = {}
        line_num = 1
        cur = 0
        for i, x in enumerate(widths):
            hash_map[chr(97+i)] = x
        for word in S:
            if cur+hash_map[word] > 100:
                line_num += 1
                cur = 0
            else:
                cur += hash_map[word]

        return line_num, 100-cur


if __name__ == '__main__':
    solution = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    ret = solution.numberOfLines(widths, "abcdefghijklmnopqrstuvwxyz")
    print(ret)