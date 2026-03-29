class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time and Space Complexity: O(rows * cols)
        visited = set()
        q = deque()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0' or (i,j) in visited: continue 
                q.append([i,j])
                count += 1
                while q:
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            if grid[nr][nc] == '1':
                                q.append([nr, nc])
        return count