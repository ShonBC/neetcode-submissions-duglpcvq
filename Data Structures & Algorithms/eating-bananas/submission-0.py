class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for val in piles:
                time += math.ceil(val / mid)
            if time <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

