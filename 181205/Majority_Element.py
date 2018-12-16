class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, cnt = nums and nums[0], 0
        for x in nums:
            if x == candidate:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                candidate = x
                cnt = 1
        return candidate