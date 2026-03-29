class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set() # int n
        dist = 0
        edges = {} # {n1, [n2, t]}
        minHeap = [] # [t, n]

        for u, v, t in times:
            if u not in edges: edges[u] = []
            edges[u].append([v, t])
        
        heapq.heappush(minHeap, [0, k])

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited: continue
            visited.add(n1)
            dist = t1
            for n2, t2 in edges.get(n1, []):
                if n2 not in visited:
                    heapq.heappush(minHeap, [t1 + t2, n2])
        return dist if len(visited) == n else -1