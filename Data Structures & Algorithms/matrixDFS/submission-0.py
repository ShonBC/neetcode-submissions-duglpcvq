class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        moves = ((0,1), (1,0),
                (0,-1), (-1,0))
        goal = (len(grid) - 1, len(grid[0]) - 1)
        ans = 0
        visited = set()
        def dfs(row, col):
            nonlocal ans
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 1 or (row, col) in visited:
                return
            if (row, col) == goal:
                ans += 1
                return
            visited.add((row, col))
            for dr, dc in moves:
                dfs(row + dr, col + dc)
            visited.remove((row, col))
        dfs(0,0)
        return ans