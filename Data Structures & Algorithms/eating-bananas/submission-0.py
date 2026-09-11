class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        k = max_pile

        l, r = 1, max_pile
        
        while l <= r:
            mid = (l + r) // 2
            total = 0
            
            for p in piles:
                total += math.ceil(p / mid)
            
            if total <= h:
                r = mid - 1
                k = min(max_pile, mid)
            elif total > h:
                l = mid + 1
        
        return k