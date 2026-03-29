class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time and Space Complexity: O(rows * cols)
        q = deque()
        visited = set()
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        time = 0
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                node = grid[i][j]
                if node == 1: fresh += 1
                elif node == 2: 
                    q.append([i,j])
                    visited.add((i,j))
        while q and fresh:
            layer = len(q)
            for _ in range(layer):
                r, c = q.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 1:
                            q.append([nr, nc])
                            fresh -= 1
            time += 1
        return time if not fresh else -1