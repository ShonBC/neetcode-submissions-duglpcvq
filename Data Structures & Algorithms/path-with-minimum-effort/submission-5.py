class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Time Complexity: O(rows * cols Log(rows * cols)) Space Complexity: O(rows * cols)
        minHeap = []
        moves = ((0,1), (1,0), (0,-1), (-1,0))
        visited = set()
        heapq.heappush(minHeap, [0, 0, 0]) # effort, row, col
        rows = len(heights) - 1
        cols = len(heights[0]) - 1
        while minHeap:
            e, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == rows and c == cols: return e
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < len(heights) and nc < len(heights[nr]) and (nr, nc) not in visited:
                    heapq.heappush(minHeap,[max(e, abs(heights[r][c] - heights[nr][nc])), nr, nc])