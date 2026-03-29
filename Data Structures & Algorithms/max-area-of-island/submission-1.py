class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        use bfs to find islands
        count number of nodes in island
        update max_area with max area found as islands are explored
        return max_area
        '''

        q = deque()
        visited = []
        moves = ((0,1), (-1,0), (0,-1), (1,0)) # right down left up
        marea = 0
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    q.append((i,j))
                    visited.append((i,j))
                    area = 1
                    while q:
                        crow, ccol = q.popleft()
                        for dr, dc in moves:
                            nr, nc = crow + dr, ccol + dc
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and (nr,nc) not in visited and grid[nr][nc] == 1):
                                area += 1
                                q.append((nr,nc))
                                visited.append((nr,nc))
                    marea = max(marea, area)
        
        return marea