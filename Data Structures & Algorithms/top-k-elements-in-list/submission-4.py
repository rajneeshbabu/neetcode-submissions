class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each number
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            
        # 2. Create buckets where the index represents the frequency
        # The maximum possible frequency is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count_map.items():
            buckets[frequency].append(num)
            
        # 3. Collect the top k frequent elements by iterating backwards
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result