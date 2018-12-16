class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_left(char):
            return char == '(' or ch == '{' or ch == '['
        def is_match(ch1, ch2):
            return ch1 == '{' and ch2 == '}' \
                or ch1 == '(' and ch2 == ')' \
                or ch1 == '[' and ch2 == ']'
        stack = []
        for ch in s:
            if is_left(ch):
                stack.append(ch)
            else:
                if len(stack) != 0 and is_match(stack[-1], ch):
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False