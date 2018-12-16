class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        balance = {5: 0, 10: 0, 20: 0}
        for money in bills:
            if money == 5:
                balance[5] += 1
            elif money == 10:
                balance[10] += 1
                balance[5] -= 1
                if balance[5] < 0:
                    return False
            elif money == 20:
                if balance[10] > 0:
                    balance[10] -= 1
                    balance[5] -= 1
                    if balance[10] < 0 or balance[5] < 0:
                        return False
                else:
                    balance[5] -= 3
                    if balance[5] < 0:
                        return False
                balance[20] += 1
        return True