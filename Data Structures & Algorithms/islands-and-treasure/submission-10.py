class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        itterate through grid to from q of all treasure chests

        dist = 0
        perform multisource BFS layer by layer from all chests at same time.
        while q 
        pop form q 
        if node is in visited or -1 skip it 
        Otherwise
        grid[node] = dist
        explore surrouinding nodes
        if new node in bounds and not in visited
        add to visited 
        if new node == INF
        add to q

        Time and Space Complexiy: O(row * col)
        '''

        dist = 0
        q = deque()
        visited = set()
        moves = ((0,1), (1,0), (0,-1), (-1,0))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i,j])
        
        while q:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                if grid[r][c] == -1: continue
                grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 2147483647:
                            q.append([nr,nc])
            dist += 1