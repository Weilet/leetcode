class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            res = str(nums[0]) + '/' + '(' + str(nums[1]) + '/'
            for i in range(2, len(nums)-1):
                res += str(nums[i]) + '/'
            res += str(nums[-1]) + ')'
            return res
