class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'

        def count(nums):
            cnt, res = 1, ''
            for i in range(1, len(nums)):
                if nums[i - 1] == nums[i]:
                    cnt += 1
                else:
                    res += str(cnt) + nums[i - 1]
                    cnt = 1
            res += str(cnt) + nums[-1]
            return res

        for _ in range(n - 1):
            ans = count(ans)
        return ans
