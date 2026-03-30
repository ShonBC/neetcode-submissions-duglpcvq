class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        moves = ((0,1,'r'),(1,0,'d'),(0,-1,'l'),(-1,0,'u'))
        minHeap = []
        visited = set()
        heapq.heappush(minHeap, [0, '', ball[0], ball[1]]) # [[num steps, path, row, col]]
        while minHeap:
            steps, path, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r,c))
            if [r, c] == hole: return path
            for dr, dc, p in moves:
                nr, nc = r + dr, c + dc
                s = 0
                goal_hit = False
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    if [nr, nc] == hole: 
                        goal_hit = True
                        break
                    nr += dr
                    nc += dc
                    s += 1
                if not goal_hit:
                    nr -= dr
                    nc -= dc
                if (nr, nc) not in visited:
                    heapq.heappush(minHeap,[steps + s, path + p, nr, nc])
        return 'impossible'