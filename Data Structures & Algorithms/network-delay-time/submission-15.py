class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time Complexity: O((E)log(E)) Space Complexity: O(V + E)
        edges = {}
        minHeap = []
        visited = set()
        cost = 0

        for u, v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append([t, v])
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            c1, v1 = heapq.heappop(minHeap)
            if v1 in visited: continue
            visited.add(v1)
            cost = c1
            for c2, v2 in edges.get(v1, []):
                nc = c1 + c2
                if v2 not in visited:
                    heapq.heappush(minHeap, [nc, v2])
        return cost if len(visited) == n else -1