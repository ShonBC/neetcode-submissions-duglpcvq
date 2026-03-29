class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        '''
        perfrom BFS
        pick a direction to move
        roll until you hit a wall
        if pos is goal return True
        if prev and new pos are in visited then skip it
        add prev and new postion to visited ((prev pos, new pos))
        pick direction to move
        Continue until goal is reached or cant move any more as all possible moves have been made
        return False

        Time Complexity: O(row * col) Space Complexity: O(row * col)
        '''
        q = deque()
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        visited = set()
        q.append(start)
        while q:
            r, c = q.popleft()
            if r == destination[0] and c == destination[1]: return True
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