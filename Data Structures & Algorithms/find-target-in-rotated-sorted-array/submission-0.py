class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pivot = l

        def binarysearch(l, r):
            while l<=r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif nums[m] <target:
                    l = m+1
                else:
                    r=m-1
            return -1
        result = binarysearch(0, pivot-1)
        if result != -1:
            return result
        return binarysearch(pivot, len(nums) - 1)
            
        