class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, x in enumerate(numbers):
            if x not in hash_map:
                hash_map[x] = [i]
            else:
                hash_map[x].append(i)
        for x in hash_map:
            if target - x in hash_map:
                if x == target - x:
                    return [hash_map[x][0] + 1, hash_map[x][1] + 1]
                return [hash_map[x][0] + 1, hash_map[target - x][0] + 1]
