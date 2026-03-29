class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {} # {u : [v, t]}
        visited = set() # u

        for u, v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append([v, t])
        
        minHeap = []
        heapq.heappush(minHeap, [0, k]) # [t, v]
        total = 0
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            print(t1, v1)
            if v1 in visited: continue
            visited.add(v1)
            total = t1
            print(total)
            for v2, t2 in edges.get(v1, []):
                if v2 not in visited:
                    heapq.heappush(minHeap, [t1 + t2, v2])
        return total if len(visited) == n else -1