class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        appear_time = {}
        word_map = re.findall(r'[!?\',;.\b]?(\w+)[!?\',;.\b]?', paragraph.lower())
        for word in word_map:
            if word not in appear_time:
                appear_time[word] = 1
            else:
                appear_time[word] += 1
        ans = ''
        max_time = 0
        for x in appear_time:
            if x not in banned and appear_time[x] > max_time:
                max_time = appear_time[x]
                ans = x
        return ans


if __name__ == '__main__':
    s = Solution()
    p = 'Bob hit a ball, the hit BALL flew far after it was hit.'
    b = ['hit']
    ret = s.mostCommonWord(p, b)
    print(ret)



