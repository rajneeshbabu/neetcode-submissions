class Solution:
    def encode(self, strs: list[str]) -> str:
        # O(N) time: Using list comprehension + join is significantly faster 
        # than looping and using the '+=' operator on strings.
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> list[str]:
        output = []
        i = 0
        s_len = len(s)
        
        while i < s_len:
            # Find the delimiter tracking the end of the length integer
            j = s.find('#', i)
            
            # Extract length and the word itself
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            output.append(word)
            
            # Fast-forward the pointer past the processed word
            i = j + 1 + length
            
        return output
