class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Time Complexity: O(rows * cols) Space Complexity: O(rows * cols)

        q = deque()
        visited = set()
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        dist = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        while q:
            layer = len(q)
            for _ in range(layer):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != -1:
                            q.append([nr, nc])
            dist += 1