class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash={}

        for i, n in enumerate(nums):
            sec = target - n
            if sec in hash:
                return [hash[sec], i]
            hash[n] = i
        