class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ''' Overall Time: O(V * E) Space: O(V + E) V = num of airports E = number of flights
        '''
        
        edges = {} # {ori: [dst, cost]}
        prices = [float('inf')] * n # prices[i] = cost to get to dst
        q = deque() # [cost, dst, stops]

        # Build adj List O(V) V = # of airports
        for o, d, c in flights:
            if o not in edges: edges[o] = []
            edges[o].append([d, c])
        
        q.append([0, src, 0])
        # Explore all nodes until q is empty -> update cost and stops along the way
        # O(V * E) time
        while q:
            c1, d1, s1 = q.popleft()
            if s1 > k: # num stops > k
                continue
            for d2, c2 in edges.get(d1, []):
                ncost = c1 + c2
                if ncost < prices[d2]:
                    prices[d2] = ncost
                    q.append([ncost, d2, s1 + 1])

        return prices[dst] if prices[dst] != float('inf') else -1