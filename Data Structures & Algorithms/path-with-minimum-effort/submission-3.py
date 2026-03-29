class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Time Complexity: O(rows * cols * log(rows * cols)) Space Complexity: O(rows * cols)
        minHeap = []
        visited = set()
        moves = ((0,1), (1,0), (0,-1,), (-1,0))
        heapq.heappush(minHeap, [0, 0, 0]) # cost, row, col

        while minHeap:
            cost, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == len(heights) - 1 and c == len(heights[0]) - 1: return cost

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if min(nr, nc) >= 0 and nr < len(heights) and nc < len(heights[nr]) and (nr, nc) not in visited:
                    ncost = abs(heights[r][c] - heights[nr][nc])
                    heapq.heappush(minHeap, [max(cost, ncost), nr, nc])