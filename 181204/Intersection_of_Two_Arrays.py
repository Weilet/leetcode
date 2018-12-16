class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        hash_map1 = {x: 1 for x in nums1}
        hash_map2 = {x: 1 for x in nums2}
        for x in hash_map1:
            if x in hash_map2:
                ans.append(x)
        return ans