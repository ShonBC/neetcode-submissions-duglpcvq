class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # Time Complexity: O(m * nlog(m * n)) Space Complexity: O(m * n)
        moves = ((0,1,'r'),(1,0,'d'),(0,-1,'l'),(-1,0,'u'))
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, [0, '', ball[0], ball[1]]) # num steps, r, c
        while minHeap:
            s, path, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if [r,c] == hole: return path
            for dr, dc, p in moves:
                nr, nc = r + dr, c + dc
                curs = 1
                hit_hole = False
                while min(nr, nc) >= 0 and nr < len(maze) and nc < len(maze[nr]) and maze[nr][nc] != 1:
                    if [nr, nc] == hole:
                        hit_hole = True
                        break
                    nr += dr
                    nc += dc
                    curs += 1
                if not hit_hole:
                    nr -= dr
                    nc -= dc
                    curs -= 1
                if (nr, nc) not in visited: 
                    heapq.heappush(minHeap, [curs + s, path + p, nr, nc])
        return "impossible"