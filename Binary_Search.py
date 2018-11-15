class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        if target not in nums:
            return -1

        while nums[mid] != target:
            if nums[mid] < target:
                start = mid + 1
                mid = (start + end) // 2
            else:
                end = mid - 1
                mid = (start + end) // 2
        return mid


if __name__ == '__main__':
    s = Solution()
    ret = s.search([-1,0,5], 5)
    print(ret)