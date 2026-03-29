class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Questions:
        No duplicate flights
        No flights from and airport to itself
        Weighted map with limited number of stops we can make
        Are all costs positive? if not then revisiting a node would be acceptible.

        q = deque() [[cost, node, num stops]]
        adj list edges = {origin : [cost, destination]}
        prices = [] list of total cost to get to each node (could be replaces with a hash map if nodes were positons in a grid or strings)

        Algorithm:
        for adj list using flights and edges

        add [0, src, 0] to q

        while q:
            pop from q
            if num stops for node is greater than k skip it
            explore next nodes with adj list
            calculate new cost to get to new node
            if new cost < old cost of the new node:
                update the price in prices and add (new cost, new node, num stops + 1) to q
        return prices[dst] if prices[dst] != float('inf') else -1

        Time Complexity: O(V * E) Space Complexity: O(V + E) V = num airports E = num of flights
        '''
        q= deque()
        edges = {}
        prices = [float('inf')] * n
        for f, t, p in flights:
            if f not in edges: edges[f] = []
            edges[f].append([p, t])
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