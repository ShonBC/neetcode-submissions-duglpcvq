class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        ans = []
        for val in nums:
            count[val] = count.get(val, 0) + 1
        
        for val, c in count.items():
            heapq.heappush(heap, [c, val])
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            c, val = heapq.heappop(heap)
            ans.append(val)
        
        return ans