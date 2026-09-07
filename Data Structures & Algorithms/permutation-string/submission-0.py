class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        # Frequency arrays for lowercase English letters (a-z)
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate frequencies for the first window
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # If the first window matches, we found a permutation
        if s1_count == s2_count:
            return True
            
        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character entering the window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove the old character leaving the window
            s2_count[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Check if the updated window matches s1
            if s1_count == s2_count:
                return True
        return False  