import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        itterate trhough nums
        count the frequeny of each number
        use array of len 2*bounded range of +-1000 + 1 to account for the 0 index
        to track the k highest frequency values
        ans array to track the k highest frequencies seen
        return the ans
        '''
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
        
        
