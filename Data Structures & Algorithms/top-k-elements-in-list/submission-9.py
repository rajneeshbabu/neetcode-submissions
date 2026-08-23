class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a standard map
        mapping = {}
        for i in nums:
            if i not in mapping:
                mapping[i]=1
            else:
                mapping[i]+=1
        mapping = mapping.items()
        ans = sorted(mapping,key= lambda mapping: mapping[1], reverse=True)
        ans = [k for k,v in ans]
        return ans[0:k]