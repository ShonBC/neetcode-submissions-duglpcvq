class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque() # [row, col]
        visited = set() # # [row, col]
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        dist = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                if grid[r][c] == -1: continue
                grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r +dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != -1:
                            q.append((nr, nc))
            dist += 1