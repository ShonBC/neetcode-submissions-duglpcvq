class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Questions:
        4 directionally connected grid? decides move set
        Can I modify the grid in place? Minor space efficiency savings by not maintianing a visited set
        grid is m X n? informs how to itterate through the grid

       Algorithm: Multi Source BFS
        define move set
        visited set
        define q = deque() which stores [[row, col]] of nodes in grid
        distance = 0

        Itterate through grid and add all treasure to q

        While q is not empty:
            layer by layer:
                pop from q
                if node is -1 skip it
                grid[node] = distance

                explore surrounding nodes:
                    if new node is in bounds and is not in visited add to visited
                    if new node is 2147483647 then add to q
            increment distance after each layer
        
        Time and Space Complexity: O(m X n)
        '''
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        visited = set()
        q= deque()
        dist = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0: 
                    q.append([i,j])
                    visited.add((i,j))
        while q:
            layer = len(q)
            for _ in range(layer):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 2147483647:
                            q.append([nr, nc])
            dist += 1