class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
        for key, value in hash_table.items():
            if value == 1:
                return key

if __name__ == '__main__':
    s = Solution()
    ret = s.singleNumber([2, 2, 1])
    print(ret)