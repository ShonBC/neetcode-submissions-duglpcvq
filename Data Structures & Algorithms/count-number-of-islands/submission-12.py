class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        visited set
        moves ()
        q = deque()
        count = 0
        Itterate through grid
        when a 1 is found, add to q and increment count
        Perform BFS on 1's to define the size of island. Add all visited nodes to the visited List
        return total count at the end
        Time Complexity: O(row * col) Space Complexity: O(row * col)
        '''
        visited = set() # ((row, col))
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        q = deque() # [[row, col]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visited or grid[i][j] != '1': continue
                visited.add((i,j))
                q.append([i,j])
                count += 1
                print(i,j, count)
                while q:
                    r, c = q.popleft()
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                            visited.add((nr,nc))
                            if grid[nr][nc] == '1':
                                q.append([nr, nc])
        return count