class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def count(word):
            ans = [0] * 52
            for i, letter in enumerate(word):
                ans[ord(letter) - ord('a') + i%2 * 52] += 1
                return ans
        return len({count(word) for word in A})

        return len(set({"".join(sorted(S[::2])) + "".join(sorted(S[1::2])) for S in A}))
