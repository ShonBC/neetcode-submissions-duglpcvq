import numpy as np
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        def distance(x, y):
            return np.sqrt(x**2 + y**2)
        
        for x, y in points:
            res.append([distance(x, y), (x,y)])
        heapq.heapify(res)
        print(res)
        ans = heapq.nsmallest(k, res)
        return [p[1] for p in ans]