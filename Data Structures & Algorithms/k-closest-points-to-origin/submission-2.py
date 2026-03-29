class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        for x,y in points:
            d = x**2 + y**2
            heapq.heappush(dist, [d,[x,y]])
            if d < dist[0][0]:
                dist[0] = [d, [x,y]]
        
        ans = heapq.nsmallest(k,dist)
        ans = [x[1] for x in ans]
        return ans