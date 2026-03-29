class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        minHeap = []
        visited = set()
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        heapq.heappush(minHeap, [0, start[0], start[1]])
        while minHeap:
            cost , r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r, c] == destination: return cost

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                steps = 0
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                    steps += 1
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited:
                    heapq.heappush(minHeap, [cost + steps, nr, nc])
        return -1