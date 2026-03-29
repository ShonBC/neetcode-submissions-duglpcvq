class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        q
        time = 0
        visited set
        moves of 4-directionaly connected grid
        total fresh bananas

        multi source bfs starting from all rotten fruit at the same time.
        itterate through grid -> when fresh banana is found increment total fresh bananas 
        if banana is rotten add to q

        while q and fresh bananas exist:
        process q layer by layer 
        pop from q
        explore surrounding nodes
        if new node is in bounds and not in visited and is fresh fruit -> 
        make rotten by decrementing total fresh bananas by 1 and add to q and visited 
        after each layer increment time by 1

        return time if total fresh bananas == 0 else -1

        Time and Space Complexity: O(row * col)
        '''

        q = deque()
        time = 0
        visited = set()
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
        fresh = 0

        # Build q
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: fresh += 1
                if grid[i][j] == 2: q.append([i, j])
        
        while q and fresh:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        q.append([nr, nc])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1