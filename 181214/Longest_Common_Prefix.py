class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs and strs[0]

        def solve(str1, str2):
            res = ''
            for i in range(min(len(str1), len(str2))):
                if str1[i] == str2[i]:
                    res += str1[i]
                else:
                    break
            return res

        for word in strs:
            ans = solve(ans, word)
        return ans if ans != [] else ""

