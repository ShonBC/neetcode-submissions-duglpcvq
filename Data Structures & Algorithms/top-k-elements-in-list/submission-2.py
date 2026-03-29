import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Count the frequency a number occurs
        freq = [[]*i for i in range(len(nums) + 1)] # the Index is the frequency and the value is a list of the numbers that occured "index" ammount of times
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items(): # for each key value pair
            freq[cnt].append(num)

        ans = []
        print(freq, count)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
            if len(ans) == k:
                return ans
        
        
