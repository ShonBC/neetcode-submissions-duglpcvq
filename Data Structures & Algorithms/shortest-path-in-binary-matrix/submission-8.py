class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        visited set() ((row, col))
        q = deque()
        length = 0
        moves = ((0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1))
        add [[0,0]] to q
        rows = len(grid) - 1
        cols = len(grid[rows]) - 1

        Perform BFS:
        while q:
            layer by layer:
            pop from q
            if node is goal return length
            elif node is 1 continue
            explore surrounding nodes
            if new node is in bounds and not in visited
            add to visited 
            if new node is 0 
            add to q
            after layer is processed increment length by 1
        
        return -1

        Time and Space Complexity: O(row * col)
        '''
        visited = set() #((row, col))
        q = deque()
        length = 1
        moves = ((0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1))
        q.append([0,0])
        rows = len(grid) - 1
        cols = len(grid[rows]) - 1
        while q:
            layer = len(q)
            for _ in range(layer):
                r, c = q.popleft()
                if (r,c) == (rows, cols): return length
                elif grid[r][c] == 1: continue
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 0:
                            q.append([nr, nc])
            length += 1
        return -1