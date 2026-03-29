class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans= 0
        visited = set()
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    ans += 1
                    visited.add((i, j))
                    q.append([i, j])
                    while q:
                        r, c = q.popleft()
                        for dr, dc in moves:
                            nr, nc = r+ dr, c + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                if grid[nr][nc] == '1':
                                    q.append([nr, nc])
        return ans