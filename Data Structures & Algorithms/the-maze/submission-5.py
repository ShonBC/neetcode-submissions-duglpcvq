class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Time Complexity: O(rows * cols)) Space Complexity: O(rows * cols)
        moves = ((0,1),(1,0),(0,-1),(-1,0))
        q = deque()
        visited = set()
        q.append(start)
        while q:
            r, c = q.popleft()
            if [r, c] == destination: return True
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                if (nr, nc) not in visited:
                    q.append([nr, nc])
                    visited.add((nr, nc))
        return False