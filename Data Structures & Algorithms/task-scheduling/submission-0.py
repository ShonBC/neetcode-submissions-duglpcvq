class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        cycles = 0
        count = Counter(tasks)
        q = deque()
        for task, total in count.items():
            print(task, total)
            heapq.heappush(maxHeap, -total)

        while maxHeap or q:
            t = heapq.heappop(maxHeap)
            print(t, cycles)
            cycles += 1
            t += 1
            if t < 0:
                q.append((-t, cycles + n)) # (# remaining tasks, next cycle it can be added to heap)
            if not maxHeap and q:
                cycles = q[0][1]
            while q and q[0][1] <= cycles + 1:
                heapq.heappush(maxHeap, -q.popleft()[0])

        return cycles
