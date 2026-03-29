class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time and Space Complexity: O(row * col)

        count = 0
        q = deque() # [[row, col]]
        visited = set() # ((row, col))
        moves = ((0,1),(1,0),(0,-1),(-1,0)) 

        '''
        Itterate through grid
        if node is in visited or equals 0 skip it
        Otherwise increment count by 1 and add it to q 
            and perform BFS to define shape of island

        while w 
        pop from q
        Otherwise explore the surrounding nodes
        if the new nodes are in bounds and not in visited
        add to visited
        if new node is equal to 1 add to q

        return count
        '''
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visited or grid[i][j] == '0': continue
                count += 1
                q.append([i,j])
                while q:
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            if grid[nr][nc] == '1':
                                q.append([nr, nc])
        return count