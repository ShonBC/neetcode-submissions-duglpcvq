class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time: O(V*E) Space: O(V+E)
        edges = {} # {from : [to, price]}
        prices = [float('inf')] * n # prices[i] = cost to get to i stop
        prices[src] = 0
        for f, t, p in flights:
            if f not in edges: edges[f] = []
            edges[f].append([t, p])
        q = deque()
        q.append([0, src, 0]) # price, from, stops
        while q:
            p1, f1, s1 = q.popleft()
            if s1 > k: continue
            for t2, p2 in edges.get(f1, []):
                ncost = p1 + p2
                if ncost < prices[t2]:
                    prices[t2] = ncost
                    q.append([ncost, t2, s1 + 1])
        return prices[dst] if prices[dst] != float('inf') else -1