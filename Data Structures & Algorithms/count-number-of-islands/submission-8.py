class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = deque()
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == '1':
                    q.append([i, j])
                    visited.add((i, j))
                    count += 1
                    while q:
                        r, c = q.popleft()
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                if grid[nr][nc] == '1':
                                    q.append([nr, nc])
        return count