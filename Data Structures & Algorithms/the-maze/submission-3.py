class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        '''
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        q = deque() since unweighted grid
        visited = set()

        Algorithm:
        add start to q
        while q:
            pop from q
            if node is goal return true
            pick a direction and roll until a wall is found then back up 1 space
            if the new node is not in visited then add to q and mark as visited
        return false

        Time and Space Complexity: O(rows * cols)
        '''
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        q = deque() 
        visited = set()

        q.append(start)
        while q:
            r, c = q.popleft()
            if [r,c] == destination: return True
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append([nr, nc])
        return False