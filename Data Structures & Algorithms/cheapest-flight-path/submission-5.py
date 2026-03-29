class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        adj list edges {ori : [prie, destination]}
        prices [price to ori initialized to float('inf')]
        q = deque [[cost, ori, num stops]]

        create adj list
        add [0, src, 0] to q

        while q:
            pop form q
            if num stops > k continue

            explore all connected destinations
            new cost = node cost + next destination cost
            if new cost < prices[next destination]:
                prices[new node] = new cost
                add [new cost, next destination, stops + 1] to q
        return prices[dst] if prices[dst] != float('inf') else -1

        Time Complexity: O(V*E) Space Complexity: O(V + E)
        '''
        edges = {}
        prices = [float('inf')] * n
        q = deque()

        for f, t, p in flights:
            if f not in edges: edges[f] = []
            edges[f].append([p,t])
        q.append([0, src, 0])
        while q:
            c1, o1, s1 = q.popleft()
            if s1 > k: continue
            for c2, o2 in edges.get(o1, []):
                newc = c1 + c2
                if newc < prices[o2]:
                    prices[o2] = newc
                    q.append([newc, o2, s1 + 1])
        return prices[dst] if prices[dst] != float('inf') else -1