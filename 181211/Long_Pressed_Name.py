class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        new_name = name and [1]
        new_typed = typed and [1]
        for i in range(1, len(name)):
            if name[i] == name[i-1]:
                new_name[-1] += 1
            else:
                new_name.append(1)
        for i in range(1, len(typed)):
            if typed[i] == typed[i-1]:
                new_typed[-1] += 1
            else:
                new_typed.append(1)
        return len(new_typed) == len(new_name) and all(x <= y for x, y in zip(new_name, new_typed))