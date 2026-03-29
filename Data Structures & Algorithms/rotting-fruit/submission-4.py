class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        count # of fresh bananas
        add all rotten to the q
        time = 0

        while q:
            for each layer:
                pop from q
                explore surrounding nodes:
                if new node is in bounds and not in visited -> make rotten, add to visited
                if fresh:
                    add to q
                    decramet # fresh bananas
            increment time
        return time if not fresh else -1

        Time and Space Complexity: O(row * col) 
        '''
        fresh = 0
        time = 0
        q = deque()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: fresh += 1
                elif grid[i][j] == 2: q.append([i,j])
        
        while q and fresh:
            layer = len(q)
            for i in range(layer):
                r, c = q.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[nr]) and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        if grid[nr][nc] == 1:
                            q.append([nr, nc])
                            grid[nr][nc] = 2
                            fresh -= 1
            time += 1
        return time if not fresh else -1