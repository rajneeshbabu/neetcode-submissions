class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
         # Dictionary to store the target character frequencies from t
        target_counts = Counter(t)
        # Dictionary to store the character frequencies of our current window
        window_counts = {}
        
        # 'required' is the number of unique characters in t that must match
        required = len(target_counts)
        # 'formed' tracks how many unique characters meet the target count in the current window
        formed = 0
        # Variables to track the best window details: (window_length, left_index, right_index)
        ans = (float('inf'), None, None)
        left = 0
        
        for right, char in enumerate(s):
            # 1. Expand the window by adding a character from the right
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character's frequency matches its required frequency in t
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
        # 2. Shrink the window from the left as long as it remains valid
            while left <= right and formed == required:
                # Update our answer if this valid window is smaller than previous ones
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # The character leaving the window
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If the character leaving breaks our required count condition
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                    
                # Move the left pointer forward
                left += 1
        # Return the smallest substring, or "" if no valid window was found
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
        