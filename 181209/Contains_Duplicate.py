class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        c = Counter(nums)
        for x in c.values():
            if x >= 2:
                return True
        return False
