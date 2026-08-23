from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prepend the length of the string and a '#' delimiter
            # Example: "neet" becomes "4#neet"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find where the delimiter '#' is located
            while s[j] != '#':
                j += 1
            
            # The characters between i and j represent the length of the word
            length = int(s[i:j])
            
            # Extract the actual word using the parsed length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Move the pointer past the extracted word to start the next one
            i = j + 1 + length
            
        return res

