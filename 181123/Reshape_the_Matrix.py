class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        if len(nums) * len(nums[0]) == r * c:
           ans, tmp = [], []
           for row in nums:
               for val in row:
                   tmp.append(val)
                   if len(tmp) % c == 0:
                       ans.append(tmp)
                       tmp = []
        else:
            return nums
        return ans