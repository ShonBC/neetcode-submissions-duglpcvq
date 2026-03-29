class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        BFS for step counting in an unweighted grid
        visited set
        moves = ((0,1),(1,0),(0,-1),(0,-1))
        q = deque() [[row, col, num steps to get to node]]
        dist = 0
        Is it a 4-directionaly connected grid? yes
        Return -1 if goal cant be reached
        can we guarentee the start and goal are inbounds and not on a wall?

        Algorithm:
        add start to q
        while q -> pop from q
        if node is goal return num steps to get to node
        pick a direction and roll until a wall is hit. Count number of empty spaces traversed
        if location has not been visited -> add to visited and queue

        return -1 if we exit while loop without finding goal

        Time Complexity: O(rows * cols) Space Complexity: O(rows * cols) 
        '''

        visited = set()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        q = deque()
        q.append([start, 0])
        visited.add(tuple(start))
        while q:
            node, steps = q.popleft()
            if node == destination: return steps
            r, c = node[0], node[1]
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                nsteps = 0
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                    nsteps += 1
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append([[nr, nc], steps + nsteps])
        return -1
