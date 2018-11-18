class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """


        return ' '.join(x for x in [x[::-1] for x in s.split()])


if __name__ == '__main__':
    solution = Solution()
    string = "Let's take LeetCode contest"
    ret = solution.reverseWords(string)
    print(ret)