class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Time Complexity: O((m * n)log(m * n)) Space Complexity: O(m * n)
        minHeap = [] # [[num steps, row, col]]
        visited = set()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        heapq.heappush(minHeap, [0, start[0], start[1]])

        while minHeap:
            steps, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r, c] == destination: return steps
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                cur = 1
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                    cur += 1
                nr -= dr
                nc -= dc
                cur -= 1
                if (nr, nc) not in visited: heapq.heappush(minHeap, [steps + cur, nr, nc])
        return -1