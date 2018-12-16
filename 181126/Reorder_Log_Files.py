class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def take_str(string):
            keyword = string.split(" ", 1)[1]
            return keyword if keyword[0].isalpha() else "z" * 32
        logs.sort(key=take_str)
        return logs
