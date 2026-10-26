class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r= 1, max(piles)
        res = r

        while l<=r:
            mid = l + (r-l)//2

            totaltime=0

            for i in piles:
                totaltime += math.ceil(i/mid)
            if totaltime<=h:
                res=min(mid, res)
                r=mid-1
            else:
                l=mid+1
        return res
        