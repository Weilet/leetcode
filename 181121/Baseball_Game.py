class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack, ans = [], 0
        for thing in ops:
            if thing == '+':
                ans += stack[-1] + stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif thing == 'D':
                ans += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif thing == 'C':
                ans -= stack[-1]
                stack.pop()
            else:
                ans += int(thing)
                stack.append(int(thing))
        return ans