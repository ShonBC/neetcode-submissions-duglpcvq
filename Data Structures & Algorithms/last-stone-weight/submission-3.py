class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones] # O(n)
        heapq.heapify(stones) # O(log(n))

        while len(stones) > 1: # O(nlog(n)) for each n in stones pop causes O(log(n)) time
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x - y)
        stones.append(0)
        return abs(stones[0])
