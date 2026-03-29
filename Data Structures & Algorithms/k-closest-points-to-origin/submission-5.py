class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Time Complexity: O(nlog(n))
        Space Complexity: O(k)
        '''
        ans = []
        heapq.heapify(ans) 
        min_dist = float('inf')
        for x, y in points: # O(n) n = len(points)
            dist = ((x**2) + (y**2))**.5
            heapq.heappush(ans, (-dist, x,y)) # O(log(n))
            if len(ans) > k: # Maintains O(k) space complexity
                heapq.heappop(ans) # O(1) operation
        return [[x,y] for d, x, y in ans]