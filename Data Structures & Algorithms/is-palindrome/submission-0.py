class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at opposite ends of the string
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 1. Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
                
            # 2. Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 3. Compare characters after converting them to lowercase
            if s[left].lower() != s[right].lower():
                return False
                
            # 4. Move both pointers closer together
            left += 1
            right -= 1
            
        return True
        