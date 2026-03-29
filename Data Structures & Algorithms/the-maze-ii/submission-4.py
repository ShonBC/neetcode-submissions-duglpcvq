class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Time Complexity: O(m * nlog(m * n)) Space Complexity: O(m * n)
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, [0, start[0], start[1]]) # num steps, r, c
        while minHeap:
            s, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r,c] == destination: return s
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                curs = 0
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                    curs += 1
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited: 
                    heapq.heappush(minHeap, [curs + s, nr, nc])
        return -1