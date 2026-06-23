class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time Complexity: O(ElogE) Space Complexity: (O(V + E))
        edges = {} # {u : t, v}
        minHeap = [] # [[t, v]]
        visited = set()
        time = 0
        for u, v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append([t, v])
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visited: continue
            visited.add(v1)
            time = t1
            for t2, v2 in edges.get(v1, []):
                t3 = t1 + t2
                heapq.heappush(minHeap, [t3, v2])
        return time if len(visited) == n else -1