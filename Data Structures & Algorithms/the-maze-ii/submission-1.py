class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        Dijkstra where cost is num steps taken
        visited set
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        minHeap [[num steps, row, col]]
        Is it a 4-directionaly connected grid? yes
        Return -1 if goal cant be reached
        can we guarentee the start and goal are inbounds and not on a wall?

        Algorithm:
        add start to min heap
        while minHeap -> pop from heap
        if node is visited -> skip it
        Otherwise add to visited
        if node is goal return num steps to get to node
        pick a direction and roll until a wall is hit. Count number of empty spaces traversed for that direction (nsteps)
        if location has not been visited -> add to minHeap

        return -1 if we exit while loop without finding goal

        Time Complexity: O((rows * cols)log(rows * cols)) Space Complexity: O(rows * cols) 
        '''

        visited = set()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        minHeap = []
        heapq.heappush(minHeap, [0, start[0], start[1]])
        while minHeap:
            steps, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r, c] == destination: return steps
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                nsteps = 0
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                    nsteps += 1
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited:
                    heapq.heappush(minHeap, [steps + nsteps, nr, nc])
        return -1
