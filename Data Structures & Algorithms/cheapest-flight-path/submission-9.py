class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time Complexity: O(V * E) Space Complexity: O(V + E)
        q = deque()
        prices = [float('inf')] * n
        edges = {}
        for f in flights:
            if f[0] not in edges: edges[f[0]] = []
            edges[f[0]].append([f[2], f[1]])
        q.append([0, src, 0]) # cost, node, num stops
        while q:
            c1, n1, s1 = q.popleft()
            print(c1, n1, s1)
            if s1 > k: continue
            for c2, n2 in edges.get(n1, []):
                ncost = c1 + c2
                if ncost < prices[n2]:
                    q.append([ncost, n2, s1 + 1])
                    prices[n2] = ncost
        return prices[dst] if prices[dst] != float('inf') else -1