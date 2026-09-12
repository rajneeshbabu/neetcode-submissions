class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. Start clean at index 0 (0 jumps taken)
        slow = 0
        fast = 0

        # Step 1: Find the meeting point inside the cycle loop
        while True:
            slow = nums[slow]          # Moves 1 hop
            fast = nums[nums[fast]]    # Moves 2 hops
            if slow == fast:
                break

        # Step 2: Find the duplicate (entrance to the loop)
        slow2 = 0                      # Starts at index 0 to match exactly
        while True:
            if slow == slow2:          # ◄ FIXED: Check BEFORE taking an extra hop!
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]




        