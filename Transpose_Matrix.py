class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[j][i] for j in range(len(A))]for i in range(len(A[0]))]


if __name__ == '__main__':
    s = Solution()
    l = [[1,2,3],[4,5,6],[7,8,9]]
    ret = s.transpose(l)
    print(ret)