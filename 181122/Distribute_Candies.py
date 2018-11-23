class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        hash_dict, cnt = {}, 0
        for candy in candies:
            if candy not in hash_dict:
                cnt += 1
                hash_dict[candy] = 1
        ans = cnt if cnt < len(candies) // 2 else len(candies) // 2
        return ans