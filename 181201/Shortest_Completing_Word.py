class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        hash_table = {}

        for ch in licensePlate.lower():
            if ch.isalpha():
                hash_table[ch] = 1 if ch not in hash_table else hash_table[ch]+1
        for word in sorted(words, key=len):
            if all(word.count(ch) >= hash_table[ch] for ch in hash_table):
                return word