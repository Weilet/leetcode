class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        row = ['', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for word in words:
            start = word.lower()[0]
            length = len(word)
            n = 1 if start in row[1] else 2 if start in row[2] else 3
            if all(x in row[n] for x in word.lower()):
                ans.append(word)
        return ans #Alaska