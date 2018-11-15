class Solution:
    def uniqueMorseRepresentations(self,   words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = []
        # alphabet_list = [chr(i) for i in range(97, 123)]
        # morse_list = [".-",  "-...",  "-.-.",  "-..",  ".",  "..-.",  "--.",  "....",  "..",  ".---",  "-.-",  ".-..",  "--",  "-.",  "---",  ".--.",  "--.-",  ".-.",  "...",  "-",  "..-",  "...-",  ".--",  "-..-",  "-.--",  "--.."]
        # correspond_table = {x: y for x, y in zip(alphabet_list, morse_list)}
        table = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        for word in words:
            morse = ''
            for letter in word:
                morse += table[letter]
            ans.add(morse)
        return len(ans)

