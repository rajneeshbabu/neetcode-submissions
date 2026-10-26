class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, s, e, target):
            if s > e:
                return -1  # Base case: target not found
            
            mid = s + (e - s) // 2  # Safe mid calculation to avoid overflow
            
            if nums[mid] == target:
                return mid  # Return the index, not nums[mid]
            elif nums[mid] > target:
                return binarysearch(nums, s, mid - 1, target)  # Search left half
            else:
                return binarysearch(nums, mid + 1, e, target)  # Search right half
        
        return binarysearch(nums, 0, len(nums) - 1, target)
        