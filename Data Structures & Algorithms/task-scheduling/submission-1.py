class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time Complexity: O(n) Space Complexity: O(n) 
        # Maintaining heap is constant since it is at most 26 elements for the 26 letters possible
        # q can be at most n elements in worst case
        maxHeap = []
        cycles = 0
        count = Counter(tasks)
        q = deque()
        for task, total in count.items():
            heapq.heappush(maxHeap, -total)

        while maxHeap or q:
            t = heapq.heappop(maxHeap)
            cycles += 1
            t += 1
            if t < 0:
                q.append((-t, cycles + n)) # (# remaining tasks, next cycle it can be added to heap)
            if not maxHeap and q:
                cycles = q[0][1]
            while q and q[0][1] <= cycles + 1:
                heapq.heappush(maxHeap, -q.popleft()[0])

        return cycles
