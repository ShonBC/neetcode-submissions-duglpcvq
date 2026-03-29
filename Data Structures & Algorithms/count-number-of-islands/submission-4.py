class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0)) # right, left, up, down
        visited = set() # (row, col) of visited positions
        q = deque()
        ans = 0
        '''
        explore (for i -> for j) until you find a 1. 
        bfs on 1's to define island and add to visited set
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Island found
                if (i, j) not in visited and grid[i][j] == '1':
                    q.append((i,j))
                    ans += 1
                    # Find island boundry
                    while q:
                        row, col = q.popleft()
                        for m in moves:
                            drow = row + m[0]
                            dcol = col + m[1]
                            # if in bounds and not visited -> add to visited
                            if 0 <= drow < len(grid) and 0 <= dcol < len(grid[0]) and (drow, dcol) not in visited:
                                visited.add((drow, dcol))
                                # if land add to q
                                if grid[drow][dcol] == '1':
                                    q.append((drow, dcol))                            
        return ans
