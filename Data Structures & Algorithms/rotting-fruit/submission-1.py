class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque() # O(r*c) space
        fresh = 0
        time = 0

        for r in range(len(grid)): # O(r*c) time
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r,c))
        
        moves = [(0,1), (-1,0), (0,-1), (1,0)] # right down left up

        while fresh > 0 and rotten:
            length = len(rotten)
            for i in range(length):
                row, col = rotten.popleft()
                for dr, dc in moves:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        # if new pos is fresh change to rotten and decrament fresh
                        fresh -= 1
                        rotten.append((nr,nc))
                        grid[nr][nc] = 2
            time += 1
        return time if fresh == 0 else -1
                
                    
                
