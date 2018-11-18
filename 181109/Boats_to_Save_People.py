class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        hash_table = {0:100}
        sum = 0
        for x in people:
            if x not in hash_table:
                hash_table[x] = 1
            else:
                hash_table[x] += 1
        print(hash_table)
        for x in people:
            if (limit-x) in hash_table and hash_table[limit-x]> 0:
                hash_table[limit-x] -= 1
                hash_table[x] -= 1
            sum += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    p = [1,2,2,3]
    l = 3
    ret = s.numRescueBoats(p, l)
    print(ret)