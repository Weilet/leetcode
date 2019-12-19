class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        len_map, pos = {}, {}
        for i, num in enumerate(nums):
            if num not in len_map:
                len_map[num] = 1
                pos[num] = i
            elif num in len_map:
                len_map[num] = i - pos[num] + 1
        max_appear = 0
        res = 100000
        for k, v in c.items():
            if v > max_appear or (v == max_appear and len_map[k] < long):
                max_appear = v
                long = len_map[k]
        return long