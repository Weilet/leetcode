from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i
            stack.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(ret)