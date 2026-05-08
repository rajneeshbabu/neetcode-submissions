class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t=target
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==t:
                     return [i, j]
        return []                      