class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0: # time and space complexity: O(1) because at most we will bit shift n 32 times
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count