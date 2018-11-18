class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash_table.keys():
                return [hash_table[rest], i]
            if nums[i] not in hash_table.keys():
                hash_table[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums_list = [3, 2, 4]
    ret = s.twoSum(nums_list, 6)
    print(ret)