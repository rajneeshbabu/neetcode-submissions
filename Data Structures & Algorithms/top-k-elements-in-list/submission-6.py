class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a standard map
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            
        # 2. Maintain a min-heap of size k
        min_heap = []
        for num, freq in count_map.items():
            # Python heaps sort by the first element in the tuple (freq)
            heapq.heappush(min_heap, (freq, num))
            
            # If the heap exceeds size k, pop the element with the lowest frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # 3. Extract the numbers from our heap of size k
        return [num for freq, num in min_heap]