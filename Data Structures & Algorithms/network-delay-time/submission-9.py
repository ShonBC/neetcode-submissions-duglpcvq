class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Dijkstra
        minHeap [[costi, vi]]
        visited (vi)
        edges {ui : [[costi, vi]]}
        time = 0

        First build the adj list (edges)

        add cost= 0 and startin node k to heap

        while minHeap exists -> pop from heap
        if node in visited -> skip it
        Otherwise set the time = the node cost1 -> for all edges associated with node:
        if new node is not in visited -> add to minHeap with cost1 + cost of new node

        return time if len(visted) ==  else -1

        Time Complexity: O((E)log(E)) Space Complexity: O(V + E)
        '''
        minHeap = [] # [[costi, vi]]
        visited = set() # [vi]
        edges = {} # {ui : [[costi, vi]]}
        time = 0

        for t in times:
            if t[0] not in edges: edges[t[0]] = []
            edges[t[0]].append([t[2], t[1]])
        
        heapq.heappush(minHeap, [0, k])
        while minHeap:
            c1, v1 = heapq.heappop(minHeap)
            if v1 in visited: continue
            visited.add(v1)
            time = c1
            for c2, v2 in edges.get(v1, []):
                if v2 not in visited:
                    heapq.heappush(minHeap, [c1 + c2, v2])
        return time if len(visited) == n else -1