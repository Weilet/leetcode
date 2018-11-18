class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums = list(nums)
        nums.sort()
        for i in range(len(nums) // 2):
            sum += min(nums[2*i], nums[2*i+1])
        return sum


if __name__ == '__main__':
    s = Solution()
    l = [1,4,3,2]
    ret = s.arrayPairSum(l)
    print(ret)