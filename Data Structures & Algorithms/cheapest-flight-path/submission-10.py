class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time Complexity: (O(V * E)) Space Complexity: O(V + E)
        edges = {} # {ori : [cost, dst]}
        q = deque() # [[cost, ori, num stops]]
        prices = [float('inf')] * n
        for o, d, c in flights:
            if o not in edges: edges[o] = []
            edges[o].append([c, d])
        q.append([0, src, 0])
        while q:
            c1, o1, s1 = q.popleft()
            if s1 > k: continue
            for c2, o2 in edges.get(o1, []):
                ncost = c1 + c2
                if ncost < prices[o2]:
                    q.append([ncost, o2, s1 + 1])
                    prices[o2] = ncost
        return prices[dst] if prices[dst] != float('inf') else -1