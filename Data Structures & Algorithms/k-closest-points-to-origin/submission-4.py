class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heapq.heapify(ans)
        min_dist = float('inf')
        for x, y in points:
            dist = ((x**2) + (y**2))**.5
            if dist < min_dist:
                ans.append((dist, x,y))
        
        ans = heapq.nsmallest(k, ans)
        return [[x,y] for d, x, y in ans]