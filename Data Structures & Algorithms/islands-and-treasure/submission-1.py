class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        dist = 0
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while q:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                if grid[r][c] == 2147483647: grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[0]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != -1:
                            q.append([nr, nc])
            dist += 1