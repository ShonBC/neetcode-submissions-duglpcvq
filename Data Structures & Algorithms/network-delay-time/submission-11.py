class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        visited set [u]
        total time
        minHeap store [[t, iu]]
        adj list edges {u : [t, v]}

        itterate through times to from adj list (O(n) Time and (O(V + E)) Space)

        add [0, k] to minHeap
        while minHeap:
            pop from minHeap
            total time = cost1
            explore all edges of node

            for each edge if edge not in visited
            add (cost1 + cost2, edge) to minHeap
        return total time if visited == n else -1

        Maintian heap is O(ElogE)
        Time Complexity: O(Elog(E)) maintian a heap of size = # of edges 
        Space Complexity: O(V + E) visited is size = # of nodes and minHeap is size of number of edges
        '''

        visited = set()
        total = 0
        minHeap = []
        edges = {}
        for u,v,t in times:
            if u not in edges: edges[u] = []
            edges[u].append([t, v])
        
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            c1, u1 = heapq.heappop(minHeap)
            if u1 in visited: continue
            total = c1
            visited.add((u1))
            for c2, v2 in edges.get(u1, []):
                if v2 not in visited:
                    print(u1, c1, v2, c2)
                    heapq.heappush(minHeap, [c1 + c2, v2])
        return total if len(visited) == n else -1