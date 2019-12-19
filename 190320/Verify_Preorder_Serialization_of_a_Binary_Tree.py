class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        data = preorder.split(',')
        for num in data:
            degree -= 1
            if degree < 0:
                break
            if num != '#':
                degree += 2
        return degree == 0
