class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        hash_table = {}
        for card in deck:
            if card not in hash_table:
                hash_table[card] = 1
            else:
                hash_table[card] += 1
        hash_table = list(hash_table.values())
        for i in range(len(hash_table)):
            if hash_table[i] == 1:
                return False
            for j in range(i+1, len(hash_table)):
                if self.has_same_factor(hash_table[i], hash_table[j]):
                    pass
                else:
                    return False
        return True

    @staticmethod
    def has_same_factor(a, b):
        for i in range(2, min(a,b)+1):
            if a % i == 0 and b % i == 0:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    l = [1]
    ret = s.hasGroupsSizeX(l)
    print(ret)