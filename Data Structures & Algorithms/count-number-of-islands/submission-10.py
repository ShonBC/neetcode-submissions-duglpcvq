class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        itterate through grid
        find a '1' and increment count
        use BFS to define the shape of the island
        add all visited positions on the grid to a visited set
        return count
        O(row X col) time and space
        '''
        count = 0
        visited = set() # (row, col)
        q = deque() # (row, col)
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '1' or (i, j) in visited:
                    continue
                q.append((i, j))
                visited.add((i, j))
                count += 1
                # BFS
                while q:
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            if grid[nr][nc] == '1':
                                q.append((nr, nc))

        return count