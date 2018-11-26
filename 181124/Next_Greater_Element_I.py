class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums1:
            found = False
            to_find = False
            for i, y in enumerate(nums2):
                if y == x:
                    to_find = True
                if y > x and to_find:
                    ans.append(y)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans

#  TODO: reduce time complex
