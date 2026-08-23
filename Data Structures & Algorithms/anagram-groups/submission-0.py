class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict where every new key automatically starts with an empty list
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. Sort the characters of the word alphabetically
            # sorted("cat") -> ['a', 'c', 't']
            # "".join(['a', 'c', 't']) -> "act"
            sorted_word = "".join(sorted(word))
            
            # 2. Use the sorted string as a key and append the original word
            anagram_map[sorted_word].append(word)
            
        # 3. Return only the grouped values as a list of lists
        return list(anagram_map.values())