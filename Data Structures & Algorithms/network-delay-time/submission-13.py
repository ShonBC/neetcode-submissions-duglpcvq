class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time Complexity: O(Elog(E)) Space Complexity: O(V + E)
        minHeap = [] # [[ti, vi]]
        visited = set()
        edges = {} # {ui : [ti, vi]}
        total = 0
        for u,v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append([t, v])
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visited: continue
            visited.add(v1)
            total = t1
            for t2, v2 in edges.get(v1, []):
                nt = t1 + t2
                heapq.heappush(minHeap, [nt, v2])
        return total if len(visited) == n else -1