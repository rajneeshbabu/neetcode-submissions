class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        nums = []
        m, n = len(nums1), len(nums2)

        # Correct pointer comparisons instead of checking list existence
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])  # Fixed from index j to i
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                
        # Append remaining elements from nums1
        while i < m:
            nums.append(nums1[i])      # Fixed from index j to i
            i += 1
            
        # Append remaining elements from nums2
        while j < n:
            nums.append(nums2[j])
            j += 1
            
        total = len(nums)
        mid = total // 2
        if total % 2 == 1:
            return float(nums[mid])
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0


