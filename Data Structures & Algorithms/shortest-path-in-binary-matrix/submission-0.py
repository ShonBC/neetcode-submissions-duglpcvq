from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        visited = set()
        queue.append((0, 0, 1))
        visited.add((0,0))
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1
        
        moves = ((1,0), (1,1), (0,1), (-1,1), 
                (-1,0), (-1,-1), (0,-1), (-1,1))
        
        while queue:
            cur_row, cur_col, cost = queue.popleft()
            if (cur_row, cur_col) == (rows - 1, cols - 1):
                return cost
            
            for drow, dcol in moves:
                new_row, new_col = cur_row + drow, cur_col + dcol

                if (new_row, new_col) not in visited and 0 <= new_row <= rows - 1 and 0 <= new_col <= cols - 1 and grid[new_row][new_col] != 1:
                    queue.append((new_row, new_col, cost + 1))
                    visited.add((new_row, new_col))
        
        return -1
