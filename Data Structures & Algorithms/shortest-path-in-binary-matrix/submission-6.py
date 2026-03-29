class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(n^2) Space Complexity: O(n^2)
        moves = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
        visited = set()
        q = deque()
        length = 1
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        q.append([0,0])
        while q:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                if grid[r][c] == 1: continue
                elif (r,c) == (rows, cols): return length
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 0: q.append([nr, nc])
            length += 1
        return -1