class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time and Space Complexity: O(rows * cols)
        q = deque()
        visited = set()
        moves = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
        q.append([0,0,1]) # r, c, length
        visited.add((0,0))
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        while q:
            layer = len(q)
            for _ in range(layer):
                r, c, l = q.popleft()
                if grid[r][c] == 1: continue
                elif r == rows and c == cols: return l
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 0:
                            q.append([nr, nc, l + 1])
        return -1