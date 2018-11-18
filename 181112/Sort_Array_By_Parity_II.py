class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        key1, key2 = [], []
        for i, val in enumerate(A):
            if (i+val) % 2 == 0:
                pass
            else:
                if i % 2 == 0:
                    key1.append(i)
                else:
                    key2.append(i)
        for x, y in zip(key1, key2):
            A[x], A[y] = A[y], A[x]
        return A


if __name__ == '__main__':
    s = Solution()
    l = [648,831,560,986,192,424,997,829,897,843]
    ret = s.sortArrayByParityII(l)
    print(ret)