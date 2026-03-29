class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Use q to allow for revisiting airports 
        q {{cost, ori, num stops}}
        build adj list edges {ori : {[cost, dst]}}
        cost list where cost[i] = price to get to destination i. Initialize to infinity

        buld adj list

        add {0, src, 0} to q
        while q not empty: 
            pop from q
            if number of stops to get to node is greater than k skip it
            Otherwise 
            explore all connected airports in edges
            for each connected airport:
                calculate the updated cost to get there
                if the new cost is less than the original cost:
                    update the price in prices[new airport] with new cost
                    add to the q with [[new cost, new airport, num stops + 1]]
            
        return cost[dst] if not equal to infinity else -1

        Time Complexity: O(V*E) Space Complexity: O(V + E)
        '''

        q = deque() # [[cost, ori, num stops]]
        edges = {} # {ori : [[cost, dst]]}
        prices = [float('inf')] * n 

        for o, d, c in flights:
            if o not in edges: edges[o] = []
            edges[o].append([c, d])
        
        q.append([0, src, 0])
        while q:
            c1, o1, s1 = q.popleft()
            print(c1, o1, s1)
            if s1 > k: continue
            for c2, o2 in edges.get(o1, []):
                newc = c1 + c2
                if newc < prices[o2]:
                    prices[o2] = newc
                    q.append([newc, o2, s1 + 1])
        return prices[dst] if prices[dst] != float('inf') else -1
