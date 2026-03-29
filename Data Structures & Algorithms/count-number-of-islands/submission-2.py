class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Island if surrounded by 0
        for i in map if i == 1 use dfs to find all 1 that form island
        incrament island and track visited nodes
        after island found check next i node not in visited 
        return count
        """

        visited = []
        q = deque()
        moves = [(0,1), (-1,0), (0,-1), (1,0)] # right down left up
        islands = 0
        for i in range(len(grid)): # O(i*j) time and space as every node would be added to visited in worst case
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == '1':
                    print(islands)
                    # Island found
                    q.append((i,j))
                    islands += 1
                    while q:
                        r, c = q.popleft()
                        for dr, dc in moves:
                            # Find island boundry
                            nr, nc = r + dr, c + dc
                            if (nr,nc) not in visited and \
                            0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
                            and grid[nr][nc] == '1':
                                visited.append((nr,nc))
                                q.append((nr,nc))
        return islands
