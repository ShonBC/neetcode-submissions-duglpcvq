class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        visited set
        dist = 0
        moves set
        q = deque
        multi-source BFS starting from all treasure chests at the same time
        traverse grid -> add all treasures to q
        Next perform BFS layer by layer: pop from q -> if node == -1 skip it
        otherwise add to visited -> assing grid[node] = dist and explore surrounding nodes.
        if nodes are in bounds, not in visited -> add to visited.
        if nodes are != -1 add them to q.
        after each layer is processed -> increment dist
        
        Time Complexity: O(row * col) Space Complexity: O(row * col)
        '''

        visited = set() # [[row, col]]
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        q = deque() # [[row, col]]
        dist = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == -1: continue
                visited.add((r, c))
                grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r + dr, c +dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != -1:
                            q.append([nr, nc])
            dist += 1                