class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)
        min_num = min(nums)
        return nums_sum - min_num * len(nums)