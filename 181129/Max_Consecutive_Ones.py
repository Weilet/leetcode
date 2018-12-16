class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ans = 0, 0
        for x in nums:
            if x == 1:
                cnt += 1
                ans = ans if ans >= cnt else cnt
            else:
                cnt = 0
        return ans