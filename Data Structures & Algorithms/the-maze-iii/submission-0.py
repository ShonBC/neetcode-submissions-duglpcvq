class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        minHeap = []
        visited = set()
        moves = ((0,1, 'r'), (1,0, 'd'), (0,-1,'l'), (-1,0, 'u'))
        path = ''
        heapq.heappush(minHeap, [0, path, ball[0], ball[1]])
        while minHeap:
            cost , p, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r, c] == hole: return p

            for dr, dc, ch in moves:
                nr, nc = r + dr, c + dc
                steps = 0
                hit_hole = False
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    steps += 1
                    if [nr, nc] == hole: 
                        hit_hole = True
                        break
                    nr += dr
                    nc += dc
                if not hit_hole:
                    nr -= dr
                    nc -= dc
                if (nr, nc) not in visited:
                    heapq.heappush(minHeap, [cost + steps, p + ch, nr, nc])
        return 'impossible'