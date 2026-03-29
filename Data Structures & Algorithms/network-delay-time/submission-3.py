class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set() # int node
        edges = {} # {n : [v, t]}
        minHeap = [] # [[t, n]]

        # Build adj list
        for n1, v1, t1 in times:
            if n1 not in edges: edges[n1] = []
            edges[n1].append([v1, t1])
        
        time = 0
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited: continue
            visited.add(n1)
            time = t1
            for n2, t2 in edges.get(n1, []):
                if n2 not in visited:
                    heapq.heappush(minHeap, [t1 + t2, n2])
        return time if len(visited) == n else -1