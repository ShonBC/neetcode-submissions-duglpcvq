class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        4-directionally connedted grid
        size row X col
        start [0,0]
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited set
        goal [row - 1 , col - 1]
        cost = max(abs(ori - dst))
        ans = max(cost seen in path)
        priority q for min heap [[cost, node]]

        Algorithm:
        add [cost of grid[0][0], (0, 0)] to min heap

        while min heap:
            pop from min heap
            if node == goal: return max cost seen in path
            explore surrounding nodes
            if node in bounds and not in visited:
                add to visited
                calculate new cost 
                if new cost < new node cost:
                    push [new cost, new node, max(new cost, max cost seen in path)]to min heap
        Time Complexity: O((row*col)log(row*col)) to maintain min heap Space Complexity: O(row*col)
        '''
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()
        minHeap = []

        heapq.heappush(minHeap, [0, [0,0]])
        while minHeap:
            c1, [r, c] = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == len(heights) - 1 and c == len(heights[0]) - 1: return c1
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < len(heights) and nc < len(heights[nr]) and (nr, nc) not in visited:
                    ncost = max(c1, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, [ncost, [nr, nc]])