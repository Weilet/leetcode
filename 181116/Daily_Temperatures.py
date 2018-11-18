class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(T)):
            if T[i] not in hash_table:
                hash_table[T[i]] = [i]
            else:
                hash_table[T[i]].append(i)
        for x in T:
            lambda x: x if x # TODO:not finished