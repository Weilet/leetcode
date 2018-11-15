class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for a in A:
            a = list(map(lambda x: 1 if x == 0 else 0, a[::-1]))
            ans.append(a)
        return ans


if __name__ == '__main__':
    s = Solution()
    l = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    ret = s.flipAndInvertImage(l)
    print(ret)