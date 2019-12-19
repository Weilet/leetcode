class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in range(len(S)):
            if S[i] == 'c':
                if not stack or stack.pop() != 'b':
                    return False
                if not stack or stack.pop() != 'a':
                    return False
            else:
                stack.append(S[i])
        return len(stack) == 0