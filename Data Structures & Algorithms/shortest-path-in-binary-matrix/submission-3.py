class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        q for nodes to explore
        visited set 
        steps = 0

        moves includes diagonal steps

        add [[0,0]] to q and start bfs layer by layer

        while q
        pop node from q
        if node == (len(grid) - 1, len(grid[0] - 1) return steps
        increment steps
        Otherwise explore surrounding nodes
        if new node is in bounds and not 1 then add to q

        return len of shortest path or -1 if goal cant be reached

        Time and Space Complexity: O(row * col) or n^2 in square grid 
        '''
        visited = set()
        q = deque()
        steps = 1
        moves = ((0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1))
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        goal = (rows, cols)
        if grid[0][0] == 1 or grid[rows][cols] == 1:
            return -1
        q.append([0,0])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r, c) == goal: return steps
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != 1: q.append([nr, nc])
            steps += 1
        return -1