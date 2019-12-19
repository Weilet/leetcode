class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP search
        def compute_next(string):
            res = [-1] * len(string)
            k, j = -1, 0
            while j < len(string) - 1:
                if k == -1 or string[j] == string[k]:
                    k, j = k + 1, j + 1
                    if string[j] == string[k]:
                        res[j] = res[k]
                    else:
                        res[j] = k
                else:
                    k = res[k]
            return res
        next = compute_next(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        return i - j if j == len(haystack) else -1

if __name__ == '__main__':
    s = Solution()
    haystack = "hello"
    needle = 'abcdabca'
    ret = s.strStr(haystack, needle)
    print(ret)
